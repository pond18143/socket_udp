from socket import * #socket libraly

serverName = '192.168.1.37' #destination
# serverName = 'localhost' #destination
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_DGRAM) #create socket for send to server
message = input('Input lowercase sentence:')
clientSocket.sendto(message.encode(),(serverName, serverPort)) #send servername,serverport into socket
modifiedMessage, serverAddress = clientSocket.recvfrom(2048) #read reply form socket to string
print(modifiedMessage.decode())
clientSocket.close() #close