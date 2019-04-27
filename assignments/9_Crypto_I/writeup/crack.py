#!/usr/bin/env python3

import hashlib
import string

def crack():
	
	with open("hashes.txt") as hfile:
		hashes = hfile.read();
		hashes = hashes.split("\n");
	
	with open("passwords.txt") as pfile:
		passwords = pfile.read();
		passwords = passwords.split("\n");
	
	characters = string.ascii_lowercase
	
	for c in characters:
		for p in passwords:
			salted = c + p;
			salted = salted.encode().rstrip();
			hashed = hashlib.sha256(salted).hexdigest().rstrip()
			if hashes.count(hashed) != 0:
				print("%s : %s" % (p, hashed));

	print("Done");

if __name__ == "__main__":
    crack()
