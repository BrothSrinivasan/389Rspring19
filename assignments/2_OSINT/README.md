OSINT (Open Source Intelligence)
======

## Assignment details

This assignment has two parts. It is due by Friday, February 22 at 11:59 PM.

To submit your homework, please follow the guidelines posted under the grading section of the syllabus.

**There will be a late penalty of 5% off per day late! Submissions received more than 3 days late will receive a 0!**

### Part 1

In class you were given an online usertag: `v0idcache`

NOTE: "briefly describe" = 2-3 sentences (and/or include screenshot(s))

Use OSINT techniques to learn as much as you can about `v0idcache` and answer the following questions:

1. What is `v0idcache`'s real name?
   Answer: Elizabeth Moffet

2. Where does `v0idcache` work? What is the URL to their website?
   Answer: Job is Banking CEO and URL is 1337bank.money
   
3. List all personal information (including social media accounts, contacts, etc) you can find about `v0idcache`. For each, briefly detail how you discovered them.

   a) She has a Twitter account. If you use checkusernames.com, then you will see she has a Twitter account linked with the tag @v0idcache.
   b) She also has a GitHub account. I found this by just searching for her in Github.
   
4. List any ( >= 1 ) IP addresses associated with the website. For each, detail the location of the server, any history in DNS, and how you discovered this information.

   Answer: 162.255.118.61-62, located in Los Angeles, CA. 216.87.155.33, located in Reston, VA. 216.87.152.33, located in Reston, VA. 142.93.136.81, located Amsterdam, NL. There is also no DNS record associated these IPs. I found this information using a combination of dnsdumpster, censys.io, and iplocation.

5. List any hidden files or directories you found on this website. For full credit, list *two* distinct flags.

   a) I found this in the /secret_directory: CMSC389R-{h1ding fil3s in r0bots L0L}
   b) I found this after logging in to website viewing source of authenticate: CMSC389R-{e@5y_p3@5y-s0urc3_l3ak}

6. What ports are open on the website? What services are running behind these ports? How did you discover this?

<<<<<<< HEAD
   Answer: Ports 22, ssh, and 80, http, 1337, waste, are open. I discovered them by using nmap on the IP then manually running nmap for ports over 1000.

7. Which operating system is running on the website? How did you discover this?
=======
7. Which operating system is running on the server that is hosting the website? How did you discover this?
>>>>>>> 927b4e4f4063f0c7b45b18f5d5846c07a6845db5

   Answer: The website runs on Linux. I know because I ran nmap with -A flag

8. **BONUS:** Did you find any other flags on your OSINT mission? (Up to 9 pts!)
   a) CMSC389R-{h1dd3n_ln plain_5ight} // in HTML code
   b) CMSC389R-{h0w_2_iNt0_DNS_r3c0Rd5} // found using DNSDumpster
   c) CMSC389R-{YWX4H3d3Bz6dx9lG32Odv0JZh} // found using Pastebin


### Part 2

Use the provided python stub code [('stub.py')](stub.py) or write your own program in another language to gain access to `v0idcache`'s server via an open port that you should have found in Part 1.

Once you have gained access to `v0idcache`'s account with the correct login credentials, you will have access to a system shell.

Use your knowledge of Linux and OSINT techniques to locate the flag file and submit its contents for points.

Your response here should briefly document how you approached and solved this part of the assignment. You should also push your bruteforce program to the "week/2/writeup" folder of your GitHub repository.

Note: If you choose to write your own program in another language, please include instructions on how to execute your program, including what version of the language you are using. You will **NOT** receive credit if the TAs cannot run your program.

If you are stuck on this part of the assignment, let us know! The facilitator staff is here to help and teach, and we are open to releasing hints as time goes on!

### Format
In the "week/2/writeup" directory of our repository there is a README.md file for you to edit and submit your homework in. Use this as a template and directly edit it with your answers. Complete your bruteforce program in this directory as well. When you've finished the assignment, push it up to your personal GitHub for us to grade.

Your responses to every prompt in this assignment should include answers to any specific questions along with a brief explanation of your thought process and how you obtained the answer.

### Scoring

Part 1 is worth 45 points, and part 2 is worth 55 points.

### Tips

Reference the slides from lecture 2 to help you effectively utilize available OSINT techniques.
