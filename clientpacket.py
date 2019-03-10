
import socket               
import random
from copy import copy,deepcopy




	
	



	
				



def substring(string1) :
	l = []
	s = ""
	string1 = string1 + " "
	for i in range(len(string1)) :	 
		if string1[i] != " ":
			s = s + string1[i]
		else:		
			l.append(int(s))
			s = ""
	return l	



def stringToMatrix(string1) :
    l4 = string1.split("_")
    l5 =[]
    for i in l4 :
        l5.append(substring(i))
    return l5


s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name/for this example
ports = 33369            #server port
portc = 32458 	   #client's own port for incoming connections (if any)
s.bind((host, portc))
s.connect((host, ports))
last_packet = " "
whileflag = 0
n = input("Enter the size of the matrix to be sent to server:\n")


#MATRIX GENERATION PART

mat= [[random.randint(1,101) for j in range(n)] for i in range(n)]

print "generated matrix",mat

#PARITY MATRIX GENERATION PART

pmat = []
plist = []

pmat = [[0 for j in range(n)] for i in range(n)]
for i in range(n):
	for j in range(n):
		temp = bin(mat[i][j])
		counter = 0
		for k in range(2,len(temp)):
			if(int(temp[k]) == 1):
				counter = counter+1
		if counter%2 == 0:
			pmat[i][j] = 1
		else:
			pmat[i][j] = 0
   
   


#PARITY APPEND GENERATION PART

plist = [0 for i in range(n)]
for i in range(n):
	tempstr = ""
	for j in range(n):
		tempstr = tempstr+str(pmat[i][j])
	plist[i] = int(tempstr,2)




#MATRIX WITH ERRORS

errorm=deepcopy(mat)

for i in range(n):
	for j in range(n):
		temp = bin(mat[i][j])	
		temp = temp[2:]
		t = list(temp)
		if(random.randint(0,100) < 5):
			if(t[0] == '0'):
				t[0] = '1'
			else:
				t[0] = '0'
		temp = "".join(str(i) for i in t)
		errorm[i][j] = int(temp,2)




errorm.append(plist) 

st_mat = []
for i in errorm :
    st_mat.append(" ".join(str(j) for j in i))
st_mat = "_".join(st_mat)

print "being sent:",st_mat


sending_str = ""
lastcount = 0

for i in range(len(st_mat)):
	if i <= 1000: 
		sending_str += st_mat[i]
	else:
		lastcount = i
		break 
s.send("MS_"+str(n)+"_"+sending_str) 

last_packet = "MS_"+str(n)+"_"+sending_str

errorplist = ""
while(whileflag == 0):
	currentpacket = s.recv(1024)
	print "incoming packet", currentpacket 
	if currentpacket[:3] == 'IHF':
		print "incorrect header format, resending packet"
		s.send(last_packet) 
	elif currentpacket[:3] == 'yes':
		sending_str = ""
		for i in range(lastcount,len(st_mat)):
			if i-lastcount <= 1000: 
				sending_str += st_mat[i]
			else:
				lastcount = i
				break 
		s.send("MS_"+str(n)+"_"+sending_str) #basic protocol header is tag+number
		
		last_packet = "MS_"+str(n)+"_"+sending_str
	elif currentpacket[:5] == 'ack_c':
		s.send("ack_s_")
		
		last_packet = "ack_s_"
	elif currentpacket[:2] == 'RM':
		lastcount = 0
		sending_str = ""
		for i in range(lastcount,len(st_mat)):
			if i-lastcount <= 1000: 
				sending_str += st_mat[i]
			else:
				lastcount = i
				break 
		s.send("MS_"+str(n)+"_"+sending_str) 
		
	elif currentpacket[:3] == "ico":
		i = 4
		str_inter = ""
		while(currentpacket[i] != '_'):
			str_inter += currentpacket[i]
			i = i+1
		inter = int(str_inter)
		if len(currentpacket) < len(str_inter)+1005:
			errorplist += currentpacket[5+len(str_inter):]
			s.send("s_int_")
			
			last_packet = "s_int_"
			print "error count:",inter
			print "error coords",errorplist
			whileflag = 1
		else:
			errorplist += currentpacket[5+len(str_inter):]
			s.send("inte_")
			
			last_packet = "inte_"
	
	else:
		c.send("IHF_")		
		print "didnt recognize, send ihf"
		last_packet = "IHF_"


s.close                     
