import socket
import threading
import json

class Client:

    def __init__(self, host, port):

        self.host = host
        self.port = port

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        print(f"Connexion à {host}:{port} ...")
        self.sock.connect((host, port))
        print("Connecté !")

        self.players = {}
        self.chat = []

        threading.Thread(target=self.listen, daemon=True).start()

    def send(self, data):
        try:
            self.sock.send((json.dumps(data) + "\n").encode())
        except:
            pass

    def listen(self):

        buffer = ""

        while True:
            try:
                data = self.sock.recv(1024).decode()
                if not data:
                    break

                buffer += data

                while "\n" in buffer:
                    msg, buffer = buffer.split("\n", 1)
                    message = json.loads(msg)

                    if message["type"] == "init":
                        self.players = message["players"]

                    elif message["type"] == "join":
                        self.players[message["player"]["id"]] = message["player"]

                    elif message["type"] == "move":
                        if message["id"] in self.players:
                            self.players[message["id"]]["pos"] = message["pos"]

                    elif message["type"] == "leave":
                        if message["id"] in self.players:
                            del self.players[message["id"]]

                    elif message["type"] == "chat":
                        self.chat.append(
                            f"{message['name']}: {message['message']}"
                        )

            except:
                break