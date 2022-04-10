from hashlib import md5
import ast


def md_encoding(s):
    return md5(s.encode("ascii")).digest()[:2]

def encapsulating(sourcePort, destinationPort, sentence):
    tcp_segment = [sourcePort,destinationPort,sentence]
    checksum = md_encoding(str(tcp_segment))
    tcp_segment = [sourcePort,destinationPort,checksum, sentence]
    return str(tcp_segment)

def decapsulating(received_segment):
    tcp_segment = ast.literal_eval(received_segment) # essa funcao aqui é pra pegar um string "[1,2,3]" e converter em lista > [1,2,3]
    received_checksum = tcp_segment[2]
    tcp_segment.pop(2)
    new_checksum = md_encoding(str(tcp_segment))
    if (new_checksum == received_checksum):
        print("Pacote integro")
        return tcp_segment
    else:
        print("Pacote não integro, reenviar novamente")
