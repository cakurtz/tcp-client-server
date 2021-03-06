from socket import *

# Server connection and socket setup to paris.cs.utexas.edu 
serverName = '128.83.144.56'
serverPort = 35603
clientSocket = socket(AF_INET, SOCK_STREAM)
try:
	clientSocket.connect((serverName,serverPort))
except Exception as err:
	print("EXCEPTION: " + str(err))
	raise SystemExit

# Create socket for server to connect to
psock = socket(AF_INET, SOCK_STREAM) # server connects to this port
sockName = clientSocket.getsockname()

# Find a successful port number to bind to and begin listening for server connection
success = 0 # Successful bind flag
count = 1 # Increment current port by count
while(success == 0):
	sockName = (sockName[0], (int(sockName[1]) + count))
	try:
		psock.bind(sockName)
		success = 1
	except Exception as err:
		count = count + 1
		continue
print('Bound to: ' + str(sockName))
psock.listen(1)

# Build request string
requestType = 'ex1'
connectionSpecifier = serverName + '-' + str(serverPort) + ' '
sockName = psock.getsockname()
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
	sys.exit()

# Accept connection on other socket from server
newsock, addr = psock.accept()
sentence = newsock.recv(1024).decode()
splitSentence = sentence.split()
print('Received: ' + sentence[0:len(sentence)-1])

# Prepare and send final outgoing string then close listening socket
sentenceTup = sentence.split()
sendString = str(int(verifyResult[3]) + 1) + ' ' + str(int(sentenceTup[4]) + 1) + '\n'
print('Sending: ' + sendString)
newsock.send(sendString.encode())
newsock.close()
psock.close()

# Get last response from server
serverResult = clientSocket.recv(1024)
print(serverResult)

# Close socket
clientSocket.close()