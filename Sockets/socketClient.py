import socket
import threading
import os

HOST = 'localhost'
PORT = 65432

def receive_data(s):
    while True:
        data = s.recv(1024)
        if data:
            print('Received from server:', data.decode())
        else:
            break

os.system('cls')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    receiver_thread = threading.Thread(target=receive_data, args=(s,))
    receiver_thread.start()

    userInput = input()
    while userInput != 'b':
        s.sendall(userInput.encode())
        userInput = input()

    receiver_thread.join()
