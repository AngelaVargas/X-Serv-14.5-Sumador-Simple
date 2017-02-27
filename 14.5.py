
#Ángela Vargas Alba
#Ejercicio 14.5 - Sumador simple

import socket
import random

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind(('localhost', 1234))

# Queue a maximum of 5 TCP connection requests

mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTML page
#  (in an infinite loop)

Count = 0;

while True:
		print ('Waiting for connections')
		(recvSocket, address) = mySocket.accept()	#Recibo un GET y devuelvo una direcc y el Socket recibido
		print ('HTTP request received')

		try:
			Peticion = recvSocket.recv(2048).decode("utf-8", "strict")	#Guardo en la variable petición los 2048 bytes que recibo del Socket
			Sumando = int(Peticion.split()[1][1:])	
			if (Count != 0):
				Suma = Count + Sumando
				recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n"	+
				"<html><body><h1>El resultado de "	+	str(Count)	+	" + "	+	str(Sumando)	+	" es "	+	str(Suma)	+
				"<h1></body></html>"	+	"\r\n",'utf-8'))
				Count = 0
			else:
				recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n"	+
				"<html><body><h1>Introduce el segundo sumando<h1>"	+
				"</body></html>"	+	"\r\n",'utf-8'))
				Count = Sumando

		except ValueError:
			print("Favicon.ico received")

recvSocket.close()
