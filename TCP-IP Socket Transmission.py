import socket
#Sequenced Commands
cmd1 = "Run 1"
cmd2 = "Run 2"
cmd3 = "Run 3"
cmd4 = "Run 4"

#Destination Settings
getIP = "127.0.0.1"  # This is a string
getPort = 8088       # This is an integer spanning 0 to 65535

return = "" # This is our output.

socket = socket.socket()
try:
    socket.connect((getIP, getPort))
except: 
    result = "Failed connecting to device."
activateCommands = [remoteMode, setMatrix, setOffset, clearBuffer]
for cmd in activateCommands:
    try:
        socket.send(cmd)
    except:
        result = "Failed activating the following command: [" + cmd + "]."
socket.close()