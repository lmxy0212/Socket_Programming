# UPD Pinger client.

import time
from socket import *
from datetime import datetime

rcvd = 1
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)  #  1 second timeout

for i in range(1,11):  # 10 pings

    try:
        message = 'Ping {0} {1}'.format(i, datetime.now().time())  # Ping msg
        start = time.time()  # start timer
        clientSocket.sendto(message.encode(), ("127.0.0.1", 12000))  # Send ping
        msg, server = clientSocket.recvfrom(1024)
        end = time.time()
        rtt = end - start
        print('Packet',i,'Response message:',msg.decode())
        print('Round Trip Time:',str(rtt) + 's \n')
        rcvd += 1

    # If data is not received back from server, print it has timed out.
    except timeout:
        print('Packet',i,'Requested timed out :(\n')

print('Summary for 10 Packets sent: received',rcvd,'packets',str(int((10-rcvd)/10*100)) + '% loss')