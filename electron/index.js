const { spawn } = require('child_process');
const { app, BrowserWindow } = require('electron');
const path = require('path');
const WebSocket = require('ws');

app.whenReady().then(() => {
    const win = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            // preload: path.join(__dirname, 'preload.js'),
            nodeIntegration: true,
            contextIsolation: false,
        }
    });

    win.loadURL('http://localhost:5173'); // Vite dev server

    ws.current = new WebSocket("ws://localhost:8000");

    ws.current.onopen = () => {
        
    };

    ws.current.onmessage = (event) => {
        
    };

    ws.current.onerror = (error) => {
        console.log("Error " + error);
    };

    ws.current.onclose = () => {
        console.log("Websocket closed");
    };

    return () => {
        ws.current.close();
    };



    // ws.on('open', () => {
    //     console.log('WebSocket connected');

    //     const ffmpeg = spawn('ffmpeg', [
    //         '-f', 'dshow',
    //         '-i', 'audio="Speakers (C-Media(R) Audio)"',
    //         '-ac', '1', // mono
    //         '-ar', '16000', // 16kHz sample rate for speech models
    //         '-f', 's16le', // PCM 16-bit little endian
    //         '-'
    //     ]);

    //     ffmpeg.stdout.on('data', chunk => {
    //         if (ws.readyState === WebSocket.OPEN) {
    //             ws.send(chunk);
    //         }
    //     });

    //     ffmpeg.stderr.on('data', data => {
    //         console.error(`ffmpeg error: ${data}`);
    //     });

    //     ffmpeg.on('close', code => {
    //         console.log(`ffmpeg exited with code ${code}`);
    //     });
    // });
});



