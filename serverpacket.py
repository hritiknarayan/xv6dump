#LAB 4
import socket               # Import socket module
import random

def listencode(list1) :
    l2 = " ".join(str(j) for j in list1)
    return l2 

def listdecode(string1) :
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



def matrixdecode(string1) :
    l4 = string1.split("_")
    l5 =[]
    for i in l4 :
        l5.append(listdecode(i))
    return l5


def paritymatgen(n,mat): 
	pmat = [[0 for j in range(n)] for i in range(n)]	
	for x in range(n):
		for y in range(n):
			temp = bin(mat[x][y])
			psum = 0
			for i in range(2,len(temp)):
				if(int(temp[i]) == 1):
					psum = psum+1
			if psum%2 == 0:
				pmat[x][y] = 1
			else:
				pmat[x][y] = 0
	return pmat

def listpgen(plist):	 
	pmat = [[0 for j in range(n)] for i in range(n)]
	c = 0
	for x in range(n):
		for y in range(n):
			temp = bin(plist[x])
			temp = temp[2:]
			c = n-len(temp)
			while(c > 0):
				temp = "0"+temp
				c = c-1
			pmat[x][y] = int(temp[y])

	return pmat
	

def calculate_intersection(n,recmat):	
	omat = [[0 for j in range(n)] for i in range(n)]
	
	plist = []
	coordlist = []
	for i in range(n+1):
		for j in range(n):
			if(i == n):
				plist.append(recmat[i][j])
			else:				
				omat[i][j] = recmat[i][j]
	
	porigmat = paritymatgen(n,omat)
	print "matrix parity generated:",porigmat
	precmat = listpgen(plist)
	print "list parity generated:",precmat	

	for x in range(n):
		for y in range(n):
			if porigmat[x][y] != precmat[x][y]:
				coordlist.append((x,y))
	print "coordlist",coordlist
	return coordlist			

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)         # Create a socket object
host = socket.gethostbyname(socket.gethostname()) # Get local machine name
port = 33369                # Reserve a port for your service.
s.bind((host, port))        
print 'host ip', host
n = 0
s.listen(5)                 # Now wait for client connection.  
while True:
   	c, addr = s.accept()     
   	print 'Connection from', addr
	close_fl = 0
	last_packet = " "
	str_mat = ""	
	
	while True:
		while True:
			recpacket = c.recv(1024)
			print "incoming packet",recpacket
			if recpacket[:3] == 'IHF':
				print "incorrect header format, resending packet"
				c.send(last_packet)
			elif recpacket[:2] == 'MS':
				i = 3
				str_n = ""
				while(recpacket[i] != '_'):
					str_n += recpacket[i]
					i = i+1
				n = int(str_n)	
				if len(recpacket) < len(str_n)+1005:
					
					str_mat += recpacket[4+len(str_n):]
					break
				else:
					
					str_mat += recpacket[4+len(str_n):]
					c.send("yes_") 
					
					last_packet = "yes_"	
			else:
				c.send("IHF_")		
				print "improper header resend packet"
				last_packet = "IHF_"
		
	
		rmat = matrixdecode(str_mat) 
		if n != len(rmat)-1:
			print n,"and",len(rmat)	
			str_mat = ""
			c.send("RM_") 
			last_packet = "RM_"
		else:		
			c.send("ack_c_") 
			
			last_packet = "ack_c_"
			break
			
	sending_str = ""
	last_sent = 0			
   
	while(close_fl == 0):
		recpacket = c.recv(1024)
		print "incoming packet", recpacket 
		if recpacket[:3] == 'IHF':
			print "improper header resend last packer"
			c.send(last_packet)    
		elif recpacket[:5] == 'ack_s':
			inter = calculate_intersection(n,rmat)
			st_inter = listencode(inter)
			for i in range(len(st_inter)):
				if i <= 1000: 
					sending_str += st_inter[i]
				else:
					last_sent = i
					break 
			c.send("ico_"+str(len(inter))+"_"+sending_str) 
			
			last_packet = "ico_"+str(len(inter))+"_"+sending_str
		elif recpacket[:4] == 'inte':
			sending_str = ""
			for i in range(last_sent,len(st_inter)):
				if i-last_sent <= 1000: 
					sending_str += st_inter[i]
				else:
					last_sent = i
					break 
			c.send("ico_"+str(len(inter))+"_"+sending_str) 
			
			last_packet = "ico_"+str(len(inter))+"_"+sending_str
		elif recpacket[:5] == 's_int':
			print "intersection/coordinates have been recieved terminate loop"
			close_fl = 1
		else:
			c.send("IHF_")		
			print "improper header format, resend packet"
			last_packet = "IHF_"
	
	
	c.close()	