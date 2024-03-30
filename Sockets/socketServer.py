import socket
import os
import threading
from collections import defaultdict

HOST = 'localhost'
PORT = 65432

connected_clients = defaultdict(socket.socket)

def handle_client(conn, addr):
  print('Connected by', addr)
  while True:
      data = conn.recv(1024)
      if data is None:
          break
      for client_socket in connected_clients.values():
          if client_socket != conn:
              try:
                  if data: print(f'Received from {client_socket}: {data}')
                  client_socket.sendall(data)
              except ConnectionError:
                  print(f"Client {client_socket.getpeername()} disconnected during send.")
                  del connected_clients[client_socket.getpeername()]

def start_server():
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.bind((HOST, PORT))
      s.listen()
      while True:
          conn, addr = s.accept()
          connected_clients[addr] = conn
          
          client_thread = threading.Thread(target=handle_client, args=(conn, addr))
          client_thread.start()

if __name__ == "__main__":
  os.system('cls')
  server_thread = threading.Thread(target=start_server)
  server_thread.start()
