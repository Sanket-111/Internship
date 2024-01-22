import socket 

ip = socket.gethostbyname (socket.gethostname())
count = 0 

for port in range(65535):	 #check for all available ports

	try:

		serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # create a new socket

		serv.bind((ip,port)) # bind socket with address
			
	except:
		
		# print('[OPEN] Port open :',port) #print open port number
		count+=1

	serv.close() #close connection
	
if count>10:
    print(1)
else :
    print(0)
