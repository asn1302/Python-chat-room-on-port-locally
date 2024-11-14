import socket
import threading

def receive_messages(conn):
    while True:
        try:
            message = conn.recv(1024).decode('utf-8')
            print(f"Received from server: {message}")
        except:
            print("Connection closed.")
            break

def start_client(username):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 12345))
    client.send(f"CONNECT {username}".encode('utf-8'))
    print(f"Connected to server as {username}.")
    threading.Thread(target=receive_messages, args=(client,)).start()
    
    while True:
        message = input(f"{username}: ")
        if message.lower() == 'exit':
            client.send(f"DISCONNECT {username}".encode('utf-8'))
            client.close()
            break
        client.send(f"MESSAGE {username} {len(message)} {message}".encode('utf-8'))
        print(f"YOU: {message}")

username = input("Enter your username: ")
start_client(username)

