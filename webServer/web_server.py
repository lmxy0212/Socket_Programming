#import socket module
from socket import *
import sys # In order to terminate the program

#Prepare a sever socket
#Fill in start
serverPort = 6789
serverIP = '127.0.0.1'
serverSocket = socket(AF_INET,SOCK_STREAM) #welcoming socket
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind((serverIP,serverPort))  #associate server IP and port num with socket
serverSocket.listen(1) #listen for TCP connection
print('server with port number',serverPort,'is up:')
#Fill in end

while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() #create connection socket in the server
    try:
        message = connectionSocket.recv(1024).decode() #receive message from socket
        print("Message:",message)
        filename = message.split()[1]
        print("file:",filename)
        f = open(filename[1:])
        outputdata = f.read() #Fill in start #Fill in end
        print("content:\n",outputdata)

        #Send one HTTP header line into socket
        #Fill in start
        header = "HTTP/1.1 200 OK\r\n\r\n"
        print(header)
        connectionSocket.send(header.encode())#sending header into socket
        #Fill in end

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        #Fill in start
        header = "HTTP/1.1 404 Not Found\r\n\r\n"
        html = "<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n"
        connectionSocket.send(header.encode()) #sending the header
        connectionSocket.send(html.encode()) #sending a 404 Not Found page
        print(header)
        # Fill in end

         # Close client socket
         # Fill in start
        connectionSocket.close()
        # Fill in end
serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data