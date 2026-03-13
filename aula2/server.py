# Servidor
import socket

HOST = "0.0.0.0"
PORT = 9007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
print("Aguardando conexões")
s.listen(1)
print("++")
conn1, addr1 = s.accept()
print("Cliente:", {addr1})

conn2, addr2 = s.accept()
print("Cliente", {addr2})
data1 = conn1.recv(1024).decode()
data2 = conn2.recv(1024).decode()

print(data1)
print(data2)

if (data1 == 'tesoura' and data2 == 'tesoura' or data1 == 'papel' and data2 == 'papel' or data1 == 'pedra' and data2 == 'pedra'):
    print("Empate")
    conn1.sendall(b'Empate')
    conn2.sendall(b'Empate')
elif (data1 == 'tesoura' and data2 == 'papel' or data1 == 'pedra' and data2 == 'tesoura' or data1 == 'papel' and data2 == 'pedra'):
    print('Cliente 1 venceu')
    conn1.sendall(b'Cliente 1 venceu')
    conn2.sendall(b'Cliente 1 venceu')
else:
    print('Cliente 2 venceu')
    conn1.sendall(b'Cliente 2 venceu')
    conn2.sendall(b'Cliente 2 venceu')


conn1.close()
conn2.close()

s.close()