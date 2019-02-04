import socket
import random

parity=' '
	

s=socket.socket()
host=socket.gethostname()
ports=12345
portc=32451

s.bind((host,portc))
s.connect((host,ports))
print 'Recieved Matrix:'
recmat= s.recv(1024)





print "Checking."



recmat=recmat.split(" ")

print recmat

reccolp=recmat[len(recmat)-1]

recrowp=recmat[len(recmat)-2]


rowpar=[0 for i in range(len(recmat)-4)]
colpar=[0 for i in range(len(recmat)-4)]


for i in range(1,len(recmat)-3):
	no=0
	for j in range(0,len(recmat)-4):
		if recmat[i][j]=="1":
			no+=1
	if no%2==0:
		rowpar[i-1]=1	
		
colparmat=[recmat[i] for i in range(1,len(recmat)-3)]	

for i in range(0,len(colparmat)):
	no=0
	for j in range(0,len(colparmat)):
		if colparmat[j][i]=="1":
			no+=1
	if no%2==0:
		colpar[i]=1	
			


for i in range(len(colparmat)):
	
	parity+=str(rowpar[i])
	
	
parity+=' '

for i in range(len(colparmat)):

	parity+=str(colpar[i])	
	
print(parity)	

recp=recrowp+' '+reccolp
		
if parity==recp:
	print "Parity verified, no errors"
	
else:

	print "Error detected"
	print "Recieved parity:",recp,"\nCalculated:",parity





s.close()
