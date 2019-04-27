#!/usr/bin/env python3

import hashlib
import string
import socket
import time

def server_crack():

	with open("passwords.txt") as pfile:
		passwords = pfile.read();
		passwords = passwords.split("\n");
	
	characters = string.ascii_lowercase;
	
	server_ip = '134.209.128.58';
	server_port = 1337;

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
	s.connect((server_ip, server_port));
	
	i = 0;
	while i <= 3:
		data = s.recv(1024).decode().rstrip();
		print(data);
		data = data[len(data)-69:len(data)-4].strip();
		for c in characters:
			for p in passwords:
				salted = c + p;
				salted = salted.encode().rstrip();
				hashed = hashlib.sha256(salted).hexdigest().rstrip();
				if data == hashed:
					print("%s:%s" % (p, hashed));
					sending = c+p+"\n";
					s.send(sending.encode());
		i = i + 1;
		
		if i == 3:
			data = s.recv(1024).decode();
			print(data);
			break;

if __name__ == "__main__":
    server_crack()
