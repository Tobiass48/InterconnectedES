# Author information
# ...
#
#
#

import socket
import time

serverName= 'servername'
serverPort= 12000
clientSocket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#placeholder Portnumber en IP
clientSocket.connect(("1.1.1.1",48484))
message1 = clientSocket.recv(1024)
print(message1.decode())
answer1_1=raw_input('Input Answer')
answer1= str(answer1_1)
clientSocket.send(answer1.encode())
while True:
    if answer1 == "1":
        l1= clientSocket.recv(1024)
        input1= clientSocket.recv(1024)

        print('From Server:', l1.decode())
        print(input1.decode())
        answer2=raw_input('Input Answer')
    
        clientSocket.send(answer2.encode())
        requested_file1= clientSocket.recv(1024)
        print('From server:', requested_file.decode())
    
    elif answer1 == "2":
        input2= clientSocket.recv(1024)
        print('From Server:', input2.decode())
        answer3=raw_input('Input Answer')
        answer3str = str(answer3)
        clientSocket.send(answer3str.encode())
        requested_file2= clientSocket.recv(1024)
        print('From Server:', requestedfile2.decode(), "has been downloaded")
        
    elif answer1 == "3":
        print('What file do you want to upload?')  
        answer3_1= raw_input('Input filename')
        answer3_1str = str(answer3_1)
        answer3_2= raw_input('Input file')
        clientSocket.send(answer3_1str.encode())
        clientSocket.send(answer3_2.encode())
                             
        file_uploaded= clientSocket.recv(1024)
        print(requestedfile2.decode())                     
        



        







clientSocket.close()
