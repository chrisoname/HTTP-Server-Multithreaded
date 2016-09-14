#import socket module
from socket import *
from threading import Thread
import time
class ClientThread(Thread):

    def __init__(self,ip,port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        print "New thread started for "+ip+ ":" + str(port)

    def run(self):
        while True:
            try:
                message = connectionSocket.recv(2048)
                print message
                if not message: break
                filename = message.split()[1]
                f = open(filename[1:])
                outputdata =  f.read() #Send one HTTP header line into socket
            #Fill in start
                extension = filename.split(".")

                if extension[1] == "jpeg":
                    headerLine = "\nHTTP/1.1 200 OK\r\n"
                    connectionSocket.send(headerLine)
                    headerLine = "Content-Type: image/jpeg;\r\n\r\n"
                    connectionSocket.send(headerLine)

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

                for i in range(0, len(outputdata)):
                    connectionSocket.send(outputdata[i])
                connectionSocket.close()
            except IOError:
                #Fill in start
                headerLine = 'HTTP/1.1 404 Not Found\r\n\r\n'
                connectionSocket.send(headerLine)
                headerLine = '404 Not Found. Check again later.'
                connectionSocket.send(headerLine) #Send response message for file not Found
                print "404"
                connectionSocket.close()         #Close client socket

        serverSocket.close()

host = '127.0.0.1'
serverPort = 8000

#Fill in start
#Prepare a sever socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((host,serverPort))
serverSocket.listen(2)
threads = []
#Fill in end

while True:
	#Establish the connection

    print "Ready to serve in port: %s" % serverPort
    connectionSocket, (ip, port) = serverSocket.accept()
    print '...connected from:', ip, port
    newthread = ClientThread(ip, port)
    newthread.start()
    time.sleep(1)
    threads.append(newthread)

    print "There are: " + str(len(threads)) + " threads running right now."

for t in threads:
    t.join()
serverSocket.close()
