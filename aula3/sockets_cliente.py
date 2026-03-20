import socket
import json

HOST = "127.0.0.1"
PORT = 9002

resposta1 = {}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
    cliente.connect((HOST, PORT))

    resposta = cliente.recv(1024).decode("utf-8")
    print(f"[Server] {resposta}")
    mensagem = input("[Cliente] CEP: ")
    resposta1["CEP"] = mensagem
    mensagem = input("[Cliente] Nome: ")
    resposta1["Nome"] = mensagem
    mensagem = input("[Cliente] Fruta: ")
    resposta1["Fruta"] = mensagem
    mensagem = input("[Cliente] Animal: ")
    resposta1["Animal"] = mensagem
    resposta1 = json.dumps(resposta1)
    cliente.sendall(resposta1.encode("utf-8"))