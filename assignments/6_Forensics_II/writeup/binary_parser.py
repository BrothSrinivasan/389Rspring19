#!/usr/bin/env python2

import sys
import struct
import datetime

def bork(msg):
	sys.exit(msg)

MAGIC = 0x8BADF00D
VERSION = 1
OFFSET = 0

if len(sys.argv) < 2:
	sys.exit("Usage: python stub.py input_file.fpff")

with open(sys.argv[1], 'rb') as fpff:
	data = fpff.read()

magic, version, date = struct.unpack_from("<LLL", data, OFFSET)
OFFSET = OFFSET + 12

if magic != MAGIC:
	bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
	bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

try:
	date = datetime.datetime.fromtimestamp(date).strftime('%c')
except:
	bork("Not UNIX date")

still_ascii = True
author = ""
i = 0

while i < 8:
	if still_ascii:
		charac = struct.unpack("<c",data[OFFSET + i])[0]
		try:
			charac = charac.decode('ascii')
			author += charac
			i = i+1
		except UnicodeDecodeError:
			still_ascii = False
	else:
		author += "\0"

OFFSET = OFFSET + i

section = struct.unpack_from("<L", data, OFFSET)[0]
OFFSET = OFFSET + 4

if int(section) <= 0:
	bork("Section is less than 0")

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))
print("DATE: %s" % date)
print("AUTHOR: %s" % author)
print("SECTION: %d" % int(section))

print("-------  BODY  -------")

curr = 0
while curr < section:
	stype, slen = struct.unpack_from("<LL", data, OFFSET)
	OFFSET = OFFSET + 8
	if slen > 0:
		if stype == 0x1:
			print("SECTION ASCII #%d" % curr)
			
			sec_ascii = struct.unpack_from(str(slen) + "s", data, OFFSET)[0]
			OFFSET = OFFSET + slen
			
			try:
				sec_ascii = sec_ascii.decode('ascii')
			except:
				bork("sec_ascii error")
			
			print("%s\n" % sec_ascii)
			
		elif stype == 0x2:
			print("SECTION UTF-8 #%d" % curr)
			
			sec_utf = struct.unpack_from(str(slen) + "s", data, OFFSET)[0]
			OFFSET = OFFSET + slen
			
			try:
				sec_utf = sec_utf.decode('utf')
			except:
				bork("sec_utf error")
			
			print("%s\n" % (curr, sec_utf))
			
		elif stype == 0x3:
			print("SECTION WORDS #%d" % curr)
			
			sec_word = struct.unpack_from(str(slen/4) + "L", data, OFFSET)[0]
			OFFSET = OFFSET + slen
			
			with open("section_words_"+ str(curr), 'wb') as f:
				f.write(bytearray([sec_word]))
				
		elif stype == 0x4:
			print("SECTION DWORDS #%d" %curr)
			
			sec_dword = struct.unpack_from(str(slen/8) + "L", data, OFFSET)[0]
			OFFSET = OFFSET + slen
			
			with open("section_dwords_"+ str(curr), 'wb') as f:
				f.write(bytearray([sec_dword]))
			
		elif stype == 0x5:
			print("SECTION DOUBLE #%d" % curr)
			
			sec_dword = struct.unpack_from(str(slen/8) + "d", data, OFFSET)[0]
			OFFSET = OFFSET + slen
			
			print("%f\n" % sec_dword)
		
		elif stype == 0x6 and slen == 16:
			print("SECTION COORD #%d" % curr)
			
			lat, lon = struct.unpack_from("dd", data, OFFSET)
			OFFSET = OFFSET + 16
			
			print("%f,%f\n" %(lat,lon))
		elif stype == 0x7 and slen == 4:
			print("SECTION REFERENCE #%d" % curr)
			
			sec_ref = struct.unpack_from("L", data, OFFSET)[0]
			OFFSET = OFFSET + 4
			
			if range(section - 1).count(sec_ref) == 0:
				bork("Invalid range")
			else:
				print("%d" % sec_ref)
		
		elif stype == 0x8:
			print("SECTION PNG #%d\n" % curr)

			png_magic = b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a'
			
			with open("section_png_" + str(curr) + ".png", 'wb') as pic:
				pic.write(png_magic)
				
				for i in range(slen):
					sec_png = struct.unpack_from("<B", data, OFFSET + i)[0]
					pic.write(bytearray([sec_png]))
				
				OFFSET = OFFSET + slen
		
		elif stype == 0x9:
			print("SECTION GIF87 #%d\n" % curr)

			gif87_magic = b'\x47\x49\x46\x38\x37\x61'
			
			with open("section_gif87_" + str(curr) + ".gif", 'wb') as pic:
				pic.write(gif87_magic)
				
				for i in range(slen):
					sec_gif87 = struct.unpack_from("b", data, OFFSET + i)[0]
					pic.write(bytearray([sec_gif87]))
				
				OFFSET = OFFSET + slen
		elif stype == 0xA:
			print("SECTION GIF89 #%d\n" % curr)

			gif89_magic = b'\x47\x49\x46\x38\x39\x61'
			
			with open("section_gif89_" + str(curr) + ".gif", 'wb') as pic:
				pic.write(gif89_magic)
				
				for i in range(slen):
					sec_gif89 = struct.unpack_from("b", data, OFFSET + i)[0]
					pic.write(bytearray([sec_gif89]))
				
				OFFSET = OFFSET + slen
		else:
			bork("something isn't right")
		
		curr = curr + 1
		
		
	
	



