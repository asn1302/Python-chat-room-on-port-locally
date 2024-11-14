import socket
import threading

clients = {}

def handle_client(conn, addr):
    print(f"New connection from {addr}")
    username = ""
    try:
        while True:
            message = conn.recv(1024).decode('utf-8')
            print(f"Others: {message}")
            if message.startswith("CONNECT"):
                username = message.split(" ")[1]
                clients[username] = conn
                print(f"{username} connected. Current clients: {list(clients.keys())}")
                broadcast(f"{username} has joined the chat.")
            elif message.startswith("MESSAGE"):
                _, sender, length, *msg_content = message.split(" ")
                message_body = " ".join(msg_content)
                broadcast(f"{sender}: {message_body}")
            elif message.startswith("DISCONNECT"):
                del clients[username]
                print(f"{username} disconnected. Current clients: {list(clients.keys())}")
                broadcast(f"{username} has left the chat.")
                break
    except:
        print("Error handling client.")
        conn.close()

def broadcast(message):
    print(f"Broadcasting message: {message}")
    for conn in clients.values():
        conn.send(message.encode('utf-8'))

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Enable port reuse
    server.bind(("localhost", 12345))
    server.listen()
    print("Server started. Waiting for connections...")
    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()

start_server()

