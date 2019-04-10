# Writeup 6 - Forensics

Name: Barath Srinivasan
Section: 0202

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Barath Srinivasan

## Assignment Writeup

### Part 1 (45 Pts)

	1)	IP address attacked is 142.93.136.81
	2)	I think they used nmap because they requested access to a lot of ports
	3)	Attacker IP is 159.203.113.181 and there are connecting from New York
	4)	port 20 is the port that they are connecting to steal the file
	5a)	the file was a jpeg file
	 b)	the photo was taken at The Hand, Rambla General Artigas, 20100 Punta Del Este, Uruguay
	 c)	The timestamp of the photo is 2018:12:23 17:16:24
	 d)	The photo was taken through an Apple iPhone 8
	 e)	The photo was taken 4.5 m below sea level
	6)	The attacker left behind a fpff file called greetz.fpff
	7)	If the users of the website either started using https rather than http that would help to make the website secure. Also, maybe using a firewall to prevent unauthorized access would also help with security.

### Part 2 (55 Pts)

	1) Code in binary_parser.py

	2) The file was generated Wed Mar 27 00:15:05 2019. It was authored by fl1nch. 
	The first section was ASCII section, with the string "Hey you, keep looking :)".
	The second section was COORD section with tuple (52.336035,4.880673).
	The third section was PNG file with binary values that was picture of testudo with the flag.
	The fourth section was ASCII with the string value "}R983CSMC_perg_tndid_u0y_yllufep0h{-R983CSMC".
	The fifth section was ASCII section with string Q01TQzM4OVIte2hleV9oM3lfeTBVX3lvdV9JX2RvbnRfbGlrZV95b3VyX2Jhc2U2NF9lbmNvZGluZ30=.
	The flag I found are:
	CMSC389R-{hey_h3y_y0U_you_I_dont_like_your_base64_encoding} // decoded from section 5
	CMSC389R-{h0pefully_y0u_didnt_grep_CMSC389R} // reverse of section three
	CMSC389R-{w31c0me_b@ck_fr0m_spring_br3ak} // in the PNG file
	
