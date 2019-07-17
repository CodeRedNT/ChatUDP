from socket import *

servidor = "127.0.0.1"
porta = 43211

obj_socket = socket(AF_INET, SOCK_DGRAM)
obj_socket.connect((servidor, porta))
saida = ""

while saida != "X":
    msg = input("Mensagem: ")
    obj_socket.sendto(msg.encode(), (servidor, porta))
    dados, origem = obj_socket.recvfrom(65535)
    print("Resposta do servidor: ", dados.decode())
    saida = input("X para fechar: ".upper())

obj_socket.close()
