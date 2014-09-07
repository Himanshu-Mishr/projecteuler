/****************************************************
*     Title: problem 21                             *           
*    Author: Himanshu Mishra                        *
*     email: himanshu.m786@gmail.com                *
****************************************************/

#include <stdio.h>
#include <stdlib.h>

int i,j,t,p,q,a,count=0;
int matrix[10000][2];
int counter = 0;
int sum = 0;

int main()  {

	for(i = 1;i <= 10000; i++)  {
		
		count = 0;
			for(j = 1;j <= i;j++)  {
                a=i%j;
                if(a==0 && i != j) {
//                	printf("%d\n", j);
                	count = count + j;
                }
    		}
//    	printf("Divisor : %d || Sum : %d\n", i,count);
    	matrix[i-1][0] = i;
    	matrix[i-1][1] = count;
    	}
//
    for (p = 0; p < 10000; p++)  {
    	for(q =0; q < 10000; q++)  {
    		if(matrix[p][0] == matrix[q][1])  {
    		 		if(matrix[q][0] == matrix[p][1])  {
    		 			sum = sum + matrix[q][0];
    		 			printf("%d\n", matrix[q][0]);
    					counter++;
    				}
    			}
    		
    	}
//    		printf("--------------------------> counter = %d  and Sum = %d \n", counter,sum);
    }
    for(t = 0;t < 10000; t++) {
    	printf("input %d || count %d\n",matrix[t][0],matrix[t][1]);
    }
	return 0;
}
