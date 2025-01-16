


import socket as SC #import the socket reference as SC

#firstly create a server
server=SC.socket(SC.AF_INET,SC.SOCK_STREAM);

# Now Bind the ip to server 
server.bind(('localhost',1096))

# listing  server here 

server.listen(2);
print("Waiting for connection ..........................");

# accept data from client
client,address=server.accept();
print("Connection eastablished.........................."); 
while True:
        try:
            data=client.recv(1024).decode()
            print(data);
        except:
            server.close();
            print("Client is not responsing");
            break;