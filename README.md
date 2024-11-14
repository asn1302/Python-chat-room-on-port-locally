# Python-chat-room-on-port-locally
You need python installed locally, does not matter the version because of the simplicity of the script, i tested this only on linux machines but i suppose it works with other operation systems. This tutorial is for linux. 

What is this? This is a small code working on open ports for in-system "comunications". The technology used it fairly easy to understand as i said it's just a simple code. 

Download the 2 files: client.py and server.py

Open a terminal an go to the directory where the 2 files are located
type: $ sudo python server.py  -- this command allows the server to be turned on on port 12345. The server will now be up and running and intercepting new users

type: $ sudo python client.py  -- this command allows a user to log into the server, by promting them with a username to chose, if we look at the server opened backround terminal we can see that <user> has logged in. The server running in the backround has more of a chatlog role. If we open another terminal tab and log with a new username, we can also see the new username being logged it. The python scripts compose more of an internal experimental chatroom between users. 

To finally the server you would have to kill every process meaning the log session for every user on the server. 

type $ sudo lsof -i :12345 

Now you see at least one PID copy it and 
type: $ sudo kill -9 <PID> 

This is it, hope you enjoy my small chatroom :)
