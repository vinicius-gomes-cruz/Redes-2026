# Cliente
import socket

HOST = "127.0.0.1"
PORT = 9006

s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

print("Escolha (pedra) (papel) (tesoura)")
texto = input()

s.sendall(texto.encode())
print(s.recv(1024).decode())

s.close()