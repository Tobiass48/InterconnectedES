# Author information
# ...
#
#
#

import socket
import time

serverName= 'servername'
serverPort= 12000
clientSocket= socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence=raw_input('Input Lowercase sentence:')
clientSocket.send(sentence.encode())
modifiedSentence= clientSocket.recv(1024)
print('From Server:', modifiedSentence.decode())
clientSocket.close()
