# Save as websocket_server.py

import asyncio
import websockets

async def echo(websocket):
    async for message in websocket:
        print(f"Received from client: {message}")
        reply = f"Server says: {message}"
        await websocket.send(reply)

async def main():
    async with websockets.serve(echo, "localhost", 8000):
        print("WebSocket server started on ws://localhost:8000")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
