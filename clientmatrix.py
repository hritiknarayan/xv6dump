import socket
import random


	

s=socket.socket()
host=socket.gethostname()
ports=12345
portc=32451

s.bind((host,portc))
s.connect((host,ports))
print 'Recieved Matrix:'
recmat= s.recv(1024)
print recmat




print "Checking."

recmat=recmat.split(" ")

reccs=recmat[len(recmat)-1]

checksum=0

for i in range(1,len(recmat)-1):
	for j in range(0,len(recmat)-2):
		if recmat[i][j]=="1":
			checksum+=1
			

			
print "Calculated Checksum:",checksum
		
if str(checksum)==reccs:
	print "Checksum verified, no errors"
	
else:

	print "Error detected"





s.close()
