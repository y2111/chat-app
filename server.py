#receving message from other users
#all for other users
#username

import sys
import socket
from _thread import *		
import pickle

def remove(user):
    client.pop(user)
    client[user].close()
def sendmessage(ulist,message,user):
        #print(ulist)
        t=user+": "+message
        if len(client)==1 or len(client)==0:
            return
        if ulist[0]=='all':
            for k in client:
                if k!=user:
                    
                    client[k].send(t.encode())
        else:
            for i in ulist:
                if i in client and i!=user:
                    
                    client[i].send(t.encode())

        return


def clientthread(user,addr):
    #welcome="Welcome to Chat Room"
    cs=client[user]
    
    
    while(1):
        try:
            message=cs.recv(2048).decode()
            #print(message)
            if message!="exit":

                rec=cs.recv(2048)
                #print(rec)
                d=pickle.loads(rec)
                #print(d)
                message=cs.recv(2048).decode()
                sendmessage(d,message, user)

            else:
                client.pop(user)
                return 
               

                
        except:
            continue

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #s.TCPServer.allow_reuse_address = True
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
except:
    print("error")	
port = 1024		
s.bind(('', port))		

s.listen(10)	
print ("Server Started listening")		
client={}


while(1):
    c, addr = s.accept()
    #uname="Enter Username"
    #c#.send(uname.encode())

    user=c.recv(1024).decode()
    print ('Got connection from'+" "+user)
    #print(addr)

    client[user]=c
    #print(client)
    welcome = 'Welcome %s!\nSend message to all users add all\nIf want to send to particular user add username\nIf you ever want to quit, type exit.' % user
    c.send(welcome.encode())
    start_new_thread(clientthread,(user,addr))
    #client.pop(user)
    
    #c.send('Thank you for connecting'.encode())

s.close()



