import random
from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

try:
    while True:
        rand = random.randint(0, 10)
        message, address = serverSocket.recvfrom(1024)
        message = message.upper()
        if (rand < 4):
            continue
        serverSocket.sendto(message, address)
finally:
    serverSocket.close()
