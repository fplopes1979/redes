from socket import *
from TCP_Methods import *

serverName = 'localhost'
serverPort = 12002
sourcePort = 12002
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

sentence = input("Olá. Insira uma frase qualquer em letras minúsculas: ")
TCP_Segment = encapsulating(sourcePort,serverPort,sentence)
print("O segmento antes de enviar: ",TCP_Segment)
clientSocket.send(TCP_Segment.encode())
received = clientSocket.recv(1024).decode()
print("O segmento recebido de resposta:", received)
tcp_received = decapsulating(received)
modifiedSentence = tcp_received[2]


print('Resposta do servidor:', modifiedSentence)
clientSocket.close()
