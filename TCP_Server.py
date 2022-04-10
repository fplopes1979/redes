from socket import *
from TCP_Methods import *

serverPort = 12002
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to receive")

while True:
    connectionSocket, addr = serverSocket.accept()
    print("Aceitou a conexao do cliente")
    received = connectionSocket.recv(1024).decode()
    print("Segmento recebido do servidor: ", received)
    tcp_received = decapsulating(received)
    print("Recebeu a frase em minuscula")
    sentence = tcp_received[2]
    capitalizedSentence = sentence.upper()
    print("Converteu em maiuscula")

    TCP_Segment = encapsulating(serverPort,tcp_received[0],capitalizedSentence)
    connectionSocket.send(TCP_Segment.encode())
    print("Mandou de volta pro cliente a frase convertida")
    connectionSocket.close()
    print("Fechou a conexao")
