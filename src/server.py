import socket
import threading
import json
import uuid

HOST = "0.0.0.0"
PORT = 5000

clients = {}
players = {}

def broadcast(data):
    for conn in clients.values():
        try:
            conn.send((json.dumps(data) + "\n").encode())
        except:
            pass

def handle_client(conn, addr):

    player_id = str(uuid.uuid4())

    players[player_id] = {
        "id": player_id,
        "name": f"Player_{player_id[:4]}",
        "pos": [0, 5, 0]
    }

    clients[player_id] = conn

    # envoyer liste joueurs existants
    conn.send((json.dumps({
        "type": "init",
        "players": players
    }) + "\n").encode())

    broadcast({
        "type": "join",
        "player": players[player_id]
    })

    buffer = ""

    while True:
        try:
            data = conn.recv(1024).decode()
            if not data:
                break

            buffer += data

            while "\n" in buffer:
                msg, buffer = buffer.split("\n", 1)
                message = json.loads(msg)

                if message["type"] == "move":
                    players[player_id]["pos"] = message["pos"]
                    broadcast({
                        "type": "move",
                        "id": player_id,
                        "pos": message["pos"]
                    })

                elif message["type"] == "chat":
                    broadcast({
                        "type": "chat",
                        "name": players[player_id]["name"],
                        "message": message["message"]
                    })

        except:
            break

    del players[player_id]
    del clients[player_id]
    broadcast({"type": "leave", "id": player_id})
    conn.close()

def start():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print("Server started on port", PORT)

    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    start()