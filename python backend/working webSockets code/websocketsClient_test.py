import asyncio
import websockets

async def test_client():
    uri = "ws://localhost:8000"
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello Server!")
        response = await websocket.recv()
        print("Response:", response)

asyncio.run(test_client())
