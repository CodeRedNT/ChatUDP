from socket import *

servidor = "127.0.0.1"
porta = 43211

obj_socket = socket(AF_INET, SOCK_DGRAM)
obj_socket.bind((servidor, porta))
print("Servidor pronto....")

while True:
    dados, origem = obj_socket.recvfrom(65535)
    print("Origem.... ", origem)
    print("Dados recebidos: ", dados.decode())
    respost = input("Digite a resposta: ")
    obj_socket.sendto(respost.encode(), origem)

obj_socket.close()