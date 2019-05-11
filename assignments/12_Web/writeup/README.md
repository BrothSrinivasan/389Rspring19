# Crypto II Writeup

Name: Barath Srinivasan
Section: 0202

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Barath

## Assignment Writeup

### Part 1 (40 Pts)
item?id=0' ||' 1=1. Originally, I was thinking about using OR, however it kept failing because the system would detect the injection. So, I gave up and just moved to part 2. In part two I noticed that URL require a ' at the end of URL to inject into. So, I put the ' in the URl when I got back to Part 1. Then I was like. okay I was still getting SQL detected. So, I decided to change the the OR to an AND just for messing around. However, the webiste wouldn't recongize it. Now I was curious. So, I was like maybe the website check specifically for that OR. So, I changed it to an operator. Then then it world. Flag: CMSC389R-{y0u_ar3_th3_SQ1_ninj@}




### Part 2 (60 Pts)

1) place <script> alert(); </script> in the search bar
Here originally I show the place query ghost text and so placed my injection in there

2) place <img src="whocare.png" onerror=alert()> as a message
Here I was trying to find an command that would execute like an HTML command. The problem was most of my commands were being sanitized. Then I remembered I could call functions form inside the HTML tags

3) replace everything after the # with 5' onerror=alert()>
This was basically the last one but an injection based. So, I got that quickly.

4) place 3'); alert('XSS in the input box.
Here I needed to scan the code and then I saw the place that was taking the input. Then I basicall messed with insertion till I got it.

5) replace confrim in URL with javascript:alert()
This took longer. But I realized that the next variable executes the confrim. So I just replaced it my code. 

6) replace /static/gadget.js with //www.google.com/jsapi?callback=alert 
This one I had to use the hints because it was tricky. Once I got the hints it was just a matter of find the right syntax to execute it.
