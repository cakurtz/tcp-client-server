Name: Coty Kurtz
UT EID: cak2493

Comments: In my program, I have it print out the strings sent to the server and all strings received from the server. I did this for easier debugging, verification, and to keep the user informed of what is going on. I made a post on piazza about if this behavior was acceptable and didn't get an answer in time, so I included files that only print out the server numbers without headers and also prints out any errors mentioned in the documentation that may occur. These can be found under the names simple_ex0.py and simple_ex1.py. The regular ex0.py and ex1.py files are used in this writeup and the results are described below. At the very bottom I have included the output of the programs without headers and strings as well as their respective logs.

Results:

###########
Exercise 0:
###########

Below is the output of one run of the ex0.py script. The servernum received in part 5 was 2695289 (found under "Second ling received" and "Servernum") and the servernum received in part 7 was 2695290 (found under "Received ack" and "Servernum+1").

Program Output:
Sending request: ex0 128.83.144.56-35603 10.147.182.223-63754 2493 C.A.Kurtz
First line received: CS 356 Server Fri Oct 06 21:53:19 CDT 2017
Second line received: OK 2494 C.A.Kurtz 2695289
Servernum: 2695289
Sending ack: ex0 2494 2695290
Received ack: CS 356 Server Fri Oct 06 21:53:19 CDT 2017 OK 2695290
Servernum+1: 2695290

The logs for ex0.py are as follows:
wireless-10-147-182-223.public.utexas.edu
Client -> Server: ex0 128.83.144.56-35603 10.147.182.223-63754 2493 C.A.Kurtz
Server -> Client: CS 356 Server Fri Oct 06 21:53:19 CDT 2017
Server -> Client: OK 2494 C.A.Kurtz 2695289
Client -> Server: ex0 2494 2695290
Server -> Client: CS 356 Server Fri Oct 06 21:53:19 CDT 2017 OK 2695290

###########
Exercise 1:
###########

Below is the output of one run of the ex1.py script. The first servernum received (part g) was 2013598, which can be found under 'Second line received'. The second servernum received (part i) was 6950784, which can be found under 'Received'. The final servernum received (part k) was 3857163, found at the very bottom.

Program Output:
Bound to: ('10.147.182.223', 63765)
Sending request: ex1 128.83.144.56-35603 10.147.182.223-63765 2493 C.A.Kurtz
First line received: CS 356 Server Fri Oct 06 21:55:32 CDT 2017
Second line received: OK 2494 C.A.Kurtz 2013598
Servernum: 2013598
Received: CS 356 server calling 6950784
Sending: 2013599 6950785

OK	3857163

The logs for ex1.py are as follows:
wireless-10-147-182-223.public.utexas.edu
Client -> Server: ex1 128.83.144.56-35603 10.147.182.223-63765 2493 C.A.Kurtz
Server -> Client: CS 356 Server Fri Oct 06 21:55:32 CDT 2017
Server -> Client: OK 2494 C.A.Kurtz 2013598
Server -> Client: Connected to a client(10.147.182.223-63765)
Server -> Client: CS 356 server calling 6950784
Client -> Server(servernum+1 newservernum+1): 2013599 6950785
Server -> Client: OK	3857163



Below is the output of the simple scripts with all 3 numbers in order as well as the logs:

Output of simple_ex0.py:
7446736
7446737

Logs:
wireless-10-147-182-223.public.utexas.edu
Client -> Server: ex0 128.83.144.56-35603 10.147.182.223-63770 2493 C.A.Kurtz
Server -> Client: CS 356 Server Fri Oct 06 22:00:39 CDT 2017
Server -> Client: OK 2494 C.A.Kurtz 7446736
Client -> Server: ex0 2494 7446737
Server -> Client: CS 356 Server Fri Oct 06 22:00:39 CDT 2017 OK 7446737

Output of simple_ex1.py:
9128587
CS 356 server calling 9305528
7146856

Logs:
wireless-10-147-182-223.public.utexas.edu
Client -> Server: ex1 128.83.144.56-35603 10.147.182.223-63788 2493 C.A.Kurtz
Server -> Client: CS 356 Server Fri Oct 06 22:03:56 CDT 2017
Server -> Client: OK 2494 C.A.Kurtz 9128587
Server -> Client: Connected to a client(10.147.182.223-63788)
Server -> Client: CS 356 server calling 9305528
Client -> Server(servernum+1 newservernum+1): 9128588 9305529
Server -> Client: OK	7146856
