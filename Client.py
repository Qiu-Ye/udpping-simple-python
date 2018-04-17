import time
from socket import *

serverName = '192.168.116.137'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)

try:
    for i in range(0, 10):
        sendTime = time.time()
        message = ('Ping %d %s' %(i+1, sendTime)).encode()
        try:
            clientSocket.sendto(message, (serverName, serverPort))
            modifuedMessage, serverAddress = clientSocket.recvfrom(1024)
            rtt = time.time() - sendTime
            print('Sequence %d: Reply from %s  RTT = %.3fs' %(i+1, serverName, rtt))
        except Exception as e:
            print('Sequence %d: Request timed out %s' %(i+1, str(e)))
    clientSocket.close()
finally:
    clientSocket.close()
