
import socket      
import pickle      
import random

# Create a socket object
s = socket.socket()        
 
# Define the port on which you want to connect
         

# connect to the server on local computer
s.connect(('127.0.0.1', 1024))
val = input("Enter username: ")
s.send(val.encode())

# receive data from the server and decoding to get the string.
print (s.recv(1024).decode())

while(1):
    
    val = input()
    if val=="send":
        s.send(val.encode())
        print('Add users to send')
        user=[]
        user = [item for item in input().split()]
    
        data=pickle.dumps(user)
        #print(data)
        s.send(data)
        message=input("Enter message: ")
        s.send(message.encode())

    elif val=="exit":
        s.send(val.encode())
        break;
    else:
        print(s.recv(2048).decode()) 
        continue
        
   
    

s.close() 
