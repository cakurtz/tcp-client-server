from socket import *
from random import *

# Server connection setup to paris.cs.utexas.edu
serverName = '128.83.144.56'
serverPort = 35603
clientSocket = socket(AF_INET, SOCK_STREAM)
try:
	clientSocket.connect((serverName,serverPort))
except Exception as err:
	print("EXCEPTION: " + str(err))
	raise SystemExit

# Build request string
requestType = 'ex0'
connectionSpecifier = serverName + '-' + str(serverPort) + ' '
sockName = clientSocket.getsockname()
connectionSpecifier = connectionSpecifier + str(sockName[0]) + '-' + str(sockName[1])
userNum = 2493
userName = 'C.A.Kurtz'
requestString = requestType + ' ' + connectionSpecifier + ' ' + str(userNum) + ' ' + userName + '\n'
print('Sending request: ' + requestString[0:len(requestString)-1])

# Send request string to server
clientSocket.send(requestString.encode())

# Receive and verify server results
serverResult = clientSocket.recv(1024)
print('First line received: ' + serverResult[0:len(serverResult)-1])
serverResult = clientSocket.recv(1024)
print('Second line received: ' + serverResult[0:len(serverResult)-1])
verifyResult = serverResult.split()
serverNum = int(verifyResult[3])
print('Servernum: ' + str(serverNum))
if(verifyResult[0] != 'OK'):
	print('ERROR: Server did not return OK')
	print('Received: ' + serverResult)
	raise SystemExit

# Build ack string and send it to server
serverNum = serverNum + 1
ackString = requestType + ' ' + verifyResult[1] + ' ' + str(serverNum) + '\n'
print('Sending ack: ' + ackString[0:len(ackString)-1])
clientSocket.send(ackString.encode())
serverResult = clientSocket.recv(1024)
print('Received ack: ' + serverResult[0:len(serverResult)-1])
verifyResult = serverResult.split()
if(verifyResult[9] == 'OK'):
	print('Servernum+1: ' + verifyResult[10])
else:
	print('ERROR: Server did not return OK')
	print('Received: ' + serverResult)


# Close socket
clientSocket.close()