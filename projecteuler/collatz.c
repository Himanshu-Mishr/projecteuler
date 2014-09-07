/***********************************************************
*     Title: euler question 14                             *           
*    Author: Himanshu Mishra                               *
*     email: himanshu.m786@gmail.com                       *
***********************************************************/

#include <stdio.h>
#include <stdlib.h>

long long int i=0; /* this is the initial input that is going to be fed */
long long int j=0;  /* this variable is going to the enter number */
long long int k=0;  /* Comment */
long long int store=0;
long long int count=0;
long long int temp=0;
long long int max=0;

int main()  {
 
	for (i = 1; i <= 1000000; i++)  {
		j = i;
		count = 0;
		temp = 0;
		store = i;
		for (k = j; k >= 1; k--)  {
			if (k == 1)  {
				++count;
     
			}
			else  {
				if (k % 2 == 0)  {
					k = store/2; 
					store = k;
					k++;
					count++;
				}
				else  { 
					if(k != 0)  {
						k = 3 * store + 1;
						store = k;
						k++;
						count++;
					}
				}      
			}
		}
		temp = count;
		if(temp > max)  {
			max = temp;
		}
		printf("\n the collatz sequence for %lld is %lld and MAX == %lld",i,count,max);

	}
	return 0;
}


