import socket
import random

x=[0]*25
y=[0]*25

for i in range(25):
	x[i]=random.randint(1,101)
	

print 'Client rng:',x
	

s=socket.socket()
host=socket.gethostname()
ports=12345
portc=32451

s.bind((host,portc))
s.connect((host,ports))
print 'Recieved random numbers:'
recvrng= s.recv(1024)
print recvrng

recvrng=recvrng.split(" ")



for i in range(1,26):
	try:
		y[i-1]=int(recvrng[i])
		
	except:
		print "Data corruption detected on one instance. Resuming computation."
		
		
	

common=[a for a in x if a in y]

commonstr="cmmn"

for i in range(len(common)):
	commonstr+=" "+str(common[i])
	
s.send(commonstr)

print s.recv(1024)




s.close()
