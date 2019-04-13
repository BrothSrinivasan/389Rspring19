# Writeup 7 - Binaries I

Name: Barath Srinivasan
Section: 0202

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Barath Srinivasan

## Assignment Writeup

### Part 1 (90 Pts)

*Put your code here as well as in main.c*
```c
#include <stdio.h>

int main()
{
	int v1 = 0xfeedface;
	int v2 = 0x1ceb00da;
	
	printf("%d\n", v1);
	printf("%d\n", v2);
	
	v1 ^= v2;
	v2 ^= v1;
	v1 ^= v2;  
	
	printf("%d\n", v1);
	printf("%d\n", v2);
	
	return 0;
}
```

### Part 2 (10 Pts)
The code is XOR swap meant to switch the values of variable v1 and v2
