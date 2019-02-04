import socket
import random

#MATRIX CREATION
matrix=" "
checksum=0

n=random.randint(3,20)

mat=[[random.randint(0,1) for i in range(n)] for j in range(n)]


parity=' '

#PARITY
rowpar=[0 for i in range(n)]
colpar=[0 for i in range(n)]
for i in range(n):
	no=0
	for j in range(n):
		if mat[i][j]==1:
			no+=1
	if no%2==0:
		rowpar[i]=1
		
		
for i in range(n):
	no=0
	for j in range(n):
		if mat[j][i]==1:
			no+=1
	if no%2==0:
		colpar[i]=1

for i in range(n):
	
	parity+=str(rowpar[i])
	
	
parity+=' '

for i in range(n):

	parity+=str(colpar[i])	
	
print(parity)	


		
#ERROR INJECTION	
ind1=random.randint(0,n-1)
ind2=random.randint(0,n-1)

mat[ind1][ind2]=1-mat[ind1][ind2]

#STRING GENERATION
for i in range(n):
	for j in range(n):
		
		
			
		matrix+=str(mat[i][j])
	matrix+=" "

	
print(matrix)






#SENDING	


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
host=socket.gethostbyname(socket.gethostname())
port = 12345


s.bind((host,port))



print 'host ip',host
s.listen(5)

flag=1
while flag==1:
	c, addr=s.accept()
	print 'Connected to',addr
	c.send(matrix)
	c.send(parity)
	
	

		
		
	
	flag=0
	



s.close() 	
	
