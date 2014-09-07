/***********************************************************
*     Title: triangular number                             *           
*    Author: Himanshu Mishra                               *
*     email: himanshu.m786@gmail.com                       *
***********************************************************/

#include <stdio.h>
#include <stdlib.h>

int sum = 0;
int i=0,j=1;
int a;
int divider_no;
int k;
int l;
int count;
int temp = 0;
int main()  {
	
	for (i = 1; i < 50000; ++i)  {
		while(1) {
			sum = sum + j;
			j++;
			if(j >= i)  {
				break;
			}
		}
//		printf("\n the triangluar number for %d  is %d", i,sum);

		divider_no = sum;
		count = 0;
		for(l=divider_no;l<=divider_no;l++)  {

//		printf("-------->The %d divider is  ",l);
			for(k=1;k<=l;k++)  {
                a=l%k;
                if(a==0) {
//                	printf("%d,", k);
                	count++;
                }
            }
            
//            printf("counter is %d\n",count-1);
		temp = count - 1;
		if(temp >= 100)  {
			printf("the triangular number for %d is %d and its number of diviser is %d\n", i,sum,temp);
			break;
		} 
        }
	}
	return 0;
}
