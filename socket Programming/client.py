import socket as SC

client=SC.socket(SC.AF_INET,SC.SOCK_STREAM)

# now connect ot local server 1096 

client.connect(('localhost',1096))
while True:
    try:
        data=input("\n--> Enter a messsage which you want to send to server ::")
        client.send(data.encode())
    except:
        client.close();
        print("Server is not found")
        break;