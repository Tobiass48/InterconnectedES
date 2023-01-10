# Author information
# ...
#
#
#

import socket

serverName = '1.1.1.1'
serverPort = 48484
serverSocket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#placeholder Portnumber en IP
serverSocket.bind(('1.1.1.1',48484))
serverSocket.listen(1)
print("The server is ready to receive")
l1 = list("filename1" , "filename2", "filename3")
#l2 = list(file1 , file2, file3)

while True:    
    connectionSocket, addr= serverSocket.accept()
    
    message1 = "What would you like to do?\n"
    "1. View Files\n"
    "2. Download\n"
    "3. Upload\n"
    "4. Chat\n"
    "5. Logout\n"
    "(press number)\n"
    connectionSocket.send(message1.encode())
    answer= connectionSocket.recv(1024).decode()
    if answer == "1":
        input1 = ("Here is the list of files")
        connectionSocket.send(l1.encode())

#       connectionSocket.send(l1.encode())
#       connectionSocket.send(input1.encode())
                   
#       answer1= connectionSocket.recv(1024).decode()
#       output1 = l1[answer]
#       connectionSocket.send(output1.encode())
    elif answer == "2":
        input2 = ("what file is requested? (Give filename)")
        connectionSocket.send(input2.encode())
        answer2= connectionSocket.recv(1024).decode()
        if answer2 in l1:
            index_2 = l1.index(answer2)
            output2 = l2[index_2]
            connectionSocket.send(output2.encode())

#send item from l1
    elif answer == "3":
        filename= connectionSocket.recv(1024).decode()
        file= connectionSocket.recv(1024).decode()
        filename_decode = filename.decode
        file_decode = file.decode
        l1.append(filename_decode)
        l2.append(file_decode)
        file_uploaded = "File has been uploaded"
        connectionSocket.send(file_uploaded.encode())

#append item onto l1
    elif answer == "4":
        print("")            
    elif answer == "5":
        print("")
        
    
    connectionSocket.close()
