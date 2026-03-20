import socket
import threading
from time import sleep
from random import randint

HOST = "0.0.0.0"
PORT = 9002

ALFABETO = "abcdefghijklmnopqrstuvwxyz"
WAITING_TIME = 3

letra = randint(0,25)
resposta = ALFABETO[letra]

def atender_cliente(conn, addr):
    print(f"[Server] jogo começou")


def iniciar_servidor():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen()

        print(f"Servidor ouvindo em {HOST}:{PORT}")
        while True:
            conn1, addr1 = server.accept()
            conn2, addr2 = server.accept()

            thread1 = threading.Thread(
                target=atender_cliente,
                args=(conn1, addr1),
                daemon=True
            )
            thread2 = threading.Thread(
                target=atender_cliente,
                args=(conn2, addr2),
                daemon=True
            )

            thread1.start()
            thread2.start()

            thread1.join()
            thread2.join()

            conn1.sendall(resposta.encode("utf-8"))
            conn2.sendall(resposta.encode("utf-8"))

            data1 = conn1.recv(1024)
            data2 = conn2.recv(1024)

            print(data1)
            print(data2)


if __name__ == "__main__":
    iniciar_servidor()