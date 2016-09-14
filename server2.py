#import socket module
from socket import *
import thread

host = '127.0.0.1'
serverPort = 8000

#Fill in start
#Prepare a sever socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((host,serverPort))

serverSocket.listen(1)


def handler(clientsocket, clientaddr):
    print "Accepted connection from: ", clientaddr
    while 1:
        data = clientsocket.recv(1024)
        msg = "You sent me: %s" % data
        clientsocket.send(msg)
	clientsocket.close()


#Fill in end
while True:
	#Establish the connection
    print "Ready to serve in port: %s" % serverPort
    connectionSocket, addr = serverSocket.accept()
    print '...connected from:', addr
    thread.start_new_thread(handler, (connectionSocket, addr))
    try:
        print "Estoy en el try"
        message = connectionSocket.recv(1024)
        #print message
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata =  f.read() #Send one HTTP header line into socket
        #Fill in start
        extension = filename.split(".")

        if extension[1] == "jpeg":

            print "mandando el header, check it out!"
            headerLine = "\nHTTP/1.1 200 OK\r\n"
            connectionSocket.send(headerLine)
            headerLine = "Content-Type: image/jpeg;\r\n\r\n"
            connectionSocket.send(headerLine)
            print "mande el header, check it out!"

        elif extension[1] == "pdf":

            headerLine = 'HTTP/1.1 200 OK\r\n'
            connectionSocket.send(headerLine)
            headerLine = "Content-Type: application/pdf\r\n\r\n"
            connectionSocket.send(headerLine)

        elif extension[1] == "mp3":

            headerLine = 'HTTP/1.1 200 OK\r\n'
            connectionSocket.send(headerLine)
            headerLine = "Content-Type: audio/mpeg3;audio/x-mpeg-3;video/mpeg;video/x-mpeg;text/xml\r\n\r\n"
            connectionSocket.send(headerLine)

        elif extension[1] == "png":
            headerLine = 'HTTP/1.1 200 OK\r\n'
            connectionSocket.send(headerLine)
            headerLine = "Content-Type: image/png\r\n\r\n"
            connectionSocket.send(headerLine)
        elif extension[1] == "txt":
            headerLine = 'HTTP/1.1 200 OK\r\n'
            connectionSocket.send(headerLine)
            headerLine = "Content-Type: text/plain\r\n\r\n"
            connectionSocket.send(headerLine)
        elif extension[1] == "gif":
            headerLine = 'HTTP/1.1 200 OK\r\n'
            connectionSocket.send(headerLine)
            headerLine = "Content-Type: image/gif\r\n\r\n"
            connectionSocket.send(headerLine)
        elif extension[1] == "wav":
            headerLine = 'HTTP/1.1 200 OK\r\n'
            connectionSocket.send(headerLine)
            headerLine = "Content-Type: audio/x-wav;audio/mpeg3;audio/x-mpeg-3;video/mpeg;video/x-mpeg;text/xml\r\n\r\n"
            connectionSocket.send(headerLine)
        elif extension[1] == "html":
            headerLine = 'HTTP/1.1 200 OK\r\n'
            connectionSocket.send(headerLine)
            headerLine = "Content-Type: text/html\r\n\r\n"
            connectionSocket.send(headerLine)

        #Fill in end
        #Fill in start
        #Fill in end
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.close()

            #    for i in range(0, len(outputdata)):
            #        connectionSocket.send(outputdata[i])
            #    connectionSocket.close()

    except IOError:
        #Fill in start
        headerLine = 'HTTP/1.1 404 Not Found\r\n\r\n'
        connectionSocket.send(headerLine)
        headerLine = '404 Not Found. Check again later.'
        connectionSocket.send(headerLine) #Send response message for file not Found
        print "404"
        connectionSocket.close()         #Close client socket

serverSocket.close()
