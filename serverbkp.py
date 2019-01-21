import socket
import random

rng="str"


for i in range(25):
	rng+=" "+str(random.randint(1,101))
	

	

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
host=socket.gethostbyname(socket.gethostname())
port = 12345


s.bind((host,port))

print 'our rng:',rng


print 'host ip',host
s.listen(5)

flag=1
while flag==1:
	c, addr=s.accept()
	print 'Connected to',addr
	c.send(rng)
	print 'Common numbers:'
	recievedcommon= c.recv(1024)
	print recievedcommon
	
	recievedcommon=recievedcommon.split(" ")
	clientrng=rng.split(" ")
	

	

	flag=0

	for i in range(1,len(recievedcommon)):
		if recievedcommon[i] not in clientrng:
			flag=1

	if flag==1:
		c.send("Wrong Numbers/None Common")
	
	else:
		c.send("Correct data recieved.")
		
		
	
	flag=0
	



s.close()	
	
