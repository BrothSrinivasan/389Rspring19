/*
 * Name: Barath Srinivasan
 * Section: 0202
 *
 * I pledge on my honor that I have not given or received any unauthorized
 * assistance on this assignment or examination.
 *
 * Digital acknowledgement: Barath Srinivasan
 */

#include <stdio.h>

int main()
{
	int v1 = 0xfeedface;
	int v2 = 0x1ceb00da;
	
	printf("a = %d\n", v1);
	printf("b = %d\n", v2);
	
	v1 ^= v2;
	v2 ^= v1;
	v1 ^= v2;  
	
	printf("a = %d\n", v1);
	printf("b = %d\n", v2);
	
	return 0;
}
