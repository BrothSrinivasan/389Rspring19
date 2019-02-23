# Writeup 2 - OSINT

Name: Barath Srinivasan
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation. --Barath Srinivasan

## Assignment Writeup

### Part 1 (45 pts)

1. What is `v0idcache`'s real name?
   Answer: Elizabeth Moffet

2. Where does `v0idcache` work? What is the URL to their website?
   Answer: Job is Banking CEO and URL is 1337bank.money
   
3. List all personal information (including social media accounts, contacts, etc) you can find about `v0idcache`. For each, briefly detail how you discovered them.

   a) She has a Twitter account. If you use checkusernames.com, then you will see she has a Twitter account linked with the tag @v0idcache.
   b) She also has a GitHub and Reddit account. I found this by just searching for her in their respective sites.
   
4. List any ( >= 1 ) IP addresses associated with the website. For each, detail the location of the server, any history in DNS, and how you discovered this information.

   Answer: 162.255.118.61-62, located in Los Angeles, CA. 216.87.155.33, located in Reston, VA. 216.87.152.33, located in Reston, VA. 142.93.136.81, located Amsterdam, NL. There is also no DNS record associated these IPs. I found this information using a combination of dnsdumpster, censys.io, and iplocation.

5. List any hidden files or directories you found on this website. For full credit, list *two* distinct flags.

   a) I found this in the /secret_directory: CMSC389R-{h1ding fil3s in r0bots L0L}
   b) I found this after logging in to website viewing source of authenticate: CMSC389R-{e@5y_p3@5y-s0urc3_l3ak}

6. What ports are open on the website? What services are running behind these ports? How did you discover this?

   Answer: Ports 22, ssh, and 80, http, 1337, waste, are open. I discovered them by using nmap on the IP, then manually running nmap for ports over 1000.

7. Which operating system is running on the website? How did you discover this?

   Answer: The website runs on Linux. I know because I ran nmap with -A flag

8. **BONUS:** Did you find any other flags on your OSINT mission? (Up to 9 pts!)
   a) CMSC389R-{h1dd3n_ln plain_5ight} // in HTML code
   b) CMSC389R-{h0w_2_iNt0_DNS_r3c0Rd5} // found using DNSDumpster
   c) CMSC389R-{YWX4H3d3Bz6dx9lG32Odv0JZh} // found using Pastebin
   d) CMSC389R-{0M3G4LUL_G3T_pWN3d_N00b} // found using Reddit

### Part 2 (75 pts)

*Please use this space to detail your approach and solutions for part 2. Don't forget to upload your completed source code to this /writeup directory as well!*

For this brutforce approach, I basically thought about it as an IO project from 216, and thought about sockets as pipes. So, basically, my approach was to open and read from the rockyou file, and push both the username and password to see if I could break in. Then I would close the socket and try again. I also outputed the data to the terminal to see which password would yield me a success. By doing this, I was able to find out the password for linkinpark. And the contents of the flag was CMSC389R-{brut3_f0rce_m4ster}.