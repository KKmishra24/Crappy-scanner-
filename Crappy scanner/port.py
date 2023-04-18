#!/bin/python3

import sys
import socket
from datetime import datetime

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) 
else:
	print("Invalid number of arguements")
	print("Syntax: python3 port.py <ip>") 

print("-" * 70)
print("Scanning target: "+target)
print("Time started: "+str(datetime.now()))
print("-" * 70)

try:
	for port in range(50,500):
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		if result == 0:
			print(f"port {port} is open")
		s.close()
		
except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()
	
except socket.gaierror:
	print("Hostname is invalid.")
	sys.exit()
	
except socket.error:
	print("Could not reach to server.")
	sys.exit()
		
