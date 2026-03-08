from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import socketio
from motor.motor_asyncio import AsyncIOMotorClient
import os

app = FastAPI()

available_origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

# CORS for FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=available_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB connection
MONGO_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
try:
    client = AsyncIOMotorClient(MONGO_URL)
    db = client.mydatabase
except Exception as e:
    print(f"Could not connect to MongoDB: {e}")

# Socket.IO
sio = socketio.AsyncServer(async_mode="asgi", cors_allowed_origins=available_origins)

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI + MongoDB + Socket.IO"}

@sio.event
async def connect(sid, environ):
    print(f"Client connected: {sid}")

@sio.event
async def disconnect(sid):
    print(f"Client disconnected: {sid}")

@sio.event
async def message(sid, data):
    print(f"Message from {sid}: {data}")
    await sio.emit("response", {"data": f"Server received: {data}"}, to=sid)

# Wrap FastAPI app with Socket.IO ASGIApp
# Uvicorn is configured to run app.main:app
# So we re-assign `app` to the new combined ASGI application
app = socketio.ASGIApp(sio, other_asgi_app=app)
