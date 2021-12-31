from socket import * #socket library

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM) #create udp socket
serverSocket.bind(('', serverPort)) #define basic for connect
print("The server is ready to receive")
while True:
    message, clientAddress = serverSocket.recvfrom(2048) #define message and address from client and read byte
    modifiedMessage = message.decode().upper() #decode and upper
    print(message.decode())
    serverSocket.sendto(modifiedMessage.encode(),clientAddress) #replyto client