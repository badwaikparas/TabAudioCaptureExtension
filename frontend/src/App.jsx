import { useState, useEffect, useRef } from "react";

function App() {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState("");
    const ws = useRef(null);

    useEffect(() => {
        ws.current = new WebSocket("ws://localhost:8000/hello");

        ws.current.onopen = () => {
            setMessages((msgs) => [...msgs, "Connected to server"]);
        };

        ws.current.onmessage = (event) => {
            setMessages((msgs) => [...msgs, `Received: ${event.data}`]);
        };

        ws.current.onerror = (error) => {
            setMessages((msgs) => [...msgs, `Error: ${error.message}`]);
        };

        ws.current.onclose = () => {
            setMessages((msgs) => [...msgs, "WebSocket closed"]);
        };

        return () => {
            ws.current.close();
        };
    }, []);

    const sendMessage = () => {
        if (ws.current && ws.current.readyState === WebSocket.OPEN) {
            ws.current.send(input);
            setMessages((msgs) => [...msgs, `Sent: ${input}`]);
            setInput("");
        } else {
            setMessages((msgs) => [...msgs, "WebSocket not connected"]);
        }
    };

    return (
        <div style={{ padding: "20px" }}>
            <h2>WebSocket React Client</h2>
            <input
                type="text"
                placeholder="Type message"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                style={{ width: "300px", marginRight: "10px" }}
            />
            <button onClick={sendMessage}>Send</button>

            <div
                style={{
                    marginTop: "20px",
                    padding: "10px",
                    border: "1px solid #ccc",
                    height: "200px",
                    overflowY: "auto",
                    whiteSpace: "pre-wrap",
                }}
            >
                {messages.map((msg, i) => (
                    <div key={i}>{msg}</div>
                ))}
            </div>
        </div>
    );
}

export default App;
