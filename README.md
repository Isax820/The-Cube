# 🧱 The Cube

> A multiplayer voxel game prototype built in Python using Modern OpenGL and TCP networking.

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![OpenGL](https://img.shields.io/badge/OpenGL-3.3+-green)
![Status](https://img.shields.io/badge/status-prototype-orange)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

---

## 📖 Overview

**The Cube** is a Minecraft-inspired multiplayer voxel prototype written in Python.  
It focuses on learning and experimenting with:

- Modern OpenGL rendering (core profile, shaders)
- Real-time multiplayer networking
- Client-server architecture
- 3D mathematics with GLM
- Basic voxel world systems

This project is educational and experimental — not a production-ready game engine.

---

## ✨ Features

- Modern OpenGL 3.3 rendering pipeline
- Custom vertex & fragment shaders
- FPS-style camera
- Multiplayer TCP server
- Unique player IDs (UUID-based)
- Real-time player position synchronization
- Integrated multiplayer chat system
- Basic voxel world rendering

---

## 🏗 Architecture

The project follows a simple client-server model.

### Server
- Handles player connections
- Assigns unique IDs
- Broadcasts movement updates
- Relays chat messages

### Client
- Connects to server
- Sends player position updates
- Renders world and other players
- Displays chat messages

### Communication Protocol
- TCP sockets
- JSON-based messages
- Threaded message handling

---

## 📂 Project Structure

```
TheCube/
│
├── server.py        # Multiplayer server
├── client.py        # Network layer
├── main.py          # Game entry point
├── camera.py        # FPS camera logic
├── shader.py        # Shader abstraction
├── world.py         # Basic voxel world
│
└── shaders/
    ├── vertex.glsl
    └── fragment.glsl
```

---

## ⚙️ Requirements

- Python 3.11+
- OpenGL 3.3 compatible GPU

Install dependencies:

```bash
pip install glfw PyOpenGL PyGLM numpy
```

---

## 🚀 Running the Project

### 1️⃣ Start the Server

```bash
python server.py
```

Expected output:
```
Server started on port 5000
```

---

### 2️⃣ Start the Client

```bash
python main.py
```

To test multiplayer, launch multiple clients.

---

## 🎮 Controls

| Key | Action |
|------|--------|
| W | Move forward |
| S | Move backward |
| A | Move left |
| D | Move right |

(Mouse look and advanced controls can be extended.)

---

## 🧠 Technical Stack

- Python
- OpenGL 3.3 Core
- GLFW (window + input)
- PyOpenGL
- PyGLM (matrix math)
- TCP Sockets
- JSON protocol

---

## ⚠️ Current Limitations

- No chunk system
- No block placement/destruction sync
- No texture atlas
- No collision physics
- No interpolation smoothing
- Server trusts clients (no validation)

This is a prototype built for experimentation and learning.

---

## 🔮 Roadmap

Planned improvements:

- Chunk-based world system
- Raycasting for block interaction
- Server tick rate system
- Position interpolation
- Persistent world save
- UI system (without GLUT)
- Player animations
- Basic physics & collisions

---

## 📜 License

MIT License — free to use and modify.

---

## 👤 Author

Personal OpenGL + networking learning project.
