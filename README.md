🧱 The Cube – Python Multiplayer Minecraft Prototype

A simple multiplayer Minecraft-like voxel game made in Python using:

OpenGL (modern shader pipeline)

GLFW

PyGLM

TCP socket networking

This project is a learning prototype focused on:

3D rendering

Client/server networking

Multiplayer synchronization

Chat system

Basic voxel world

🚀 Features

Modern OpenGL rendering (no deprecated pipeline)

Shader-based projection / view / model matrices

Multiplayer TCP server

Unique player IDs (UUID)

Real-time player position synchronization

Global chat system

Basic FPS movement

Simple voxel world

📁 Project Structure

TheCube/

server.py → Multiplayer server

client.py → Network client

main.py → Game entry point

camera.py → FPS camera

shader.py → Shader loader

world.py → Simple voxel world

shaders/

vertex.glsl

fragment.glsl

📦 Requirements

Python 3.11+ recommended

Install dependencies:

pip install glfw PyOpenGL PyGLM numpy

▶️ How To Run

1️⃣ Start the server

Open a terminal:

python server.py

You should see:
Server started on port 5000

2️⃣ Start the game client

In another terminal:

python main.py

3️⃣ Multiplayer Test

Open multiple game windows to simulate multiple players.

🎮 Controls

W → Move forward
S → Move backward
A → Move left
D → Move right

(Chat system implemented but can be extended further.)

🛠 Technical Overview

Rendering:

OpenGL 3.3 Core

Vertex + Fragment shaders

Projection / View / Model matrices handled with PyGLM

VBO / VAO / EBO

Networking:

TCP sockets

JSON message protocol

Threaded server

Broadcast-based synchronization

Message types:

init

join

move

leave

chat

⚠️ Limitations

This is a prototype project.

Not yet implemented:

Chunk system

Texture atlas

Block breaking / placing

Physics & collisions

Mouse look

Interpolation smoothing

Security validation (server trusts clients)

🧠 Future Improvements

Chunk-based world optimization

Raycasting system

Player interpolation

Server tick rate

Block placement/destruction sync

Persistent world save

UI system

Better input handling

📜 License

This project have a MIT License
