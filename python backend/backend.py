from fastapi import FastAPI, WebSocket
import uvicorn

app = FastAPI()

# @app.websocket("/audio")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     print("Client connected")

#     with open("live_stream.raw", "wb") as f:
#         while True:
#             try:
#                 data = await websocket.receive_bytes()
#                 f.write(data)
#                 # Optional: feed to diarization/transcription model here
#             except Exception as e:
#                 print(f"WebSocket error: {e}")
#                 break

#     print("Client disconnected")

@app.websocket("/hello")  # <-- This must match exactly
async def hello(websocket: WebSocket):
    await websocket.accept()
    print("Client connected")
    await websocket.send_text("hello123")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
