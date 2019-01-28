import socket
import random

#MATRIX CREATION
matrix=" "
checksum=0

n=random.randint(3,20)

mat=[[random.randint(0,1) for i in range(n)] for j in range(n)]




#CHECKSUM
for i in range(n):
	for j in range(n):
		if mat[i][j]==1:
			checksum+=1
		
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
	c.send(str(checksum))
	
	

		
		
	
	flag=0
	



s.close() 	
	
