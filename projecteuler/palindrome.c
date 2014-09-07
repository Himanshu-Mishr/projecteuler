/***************************************************
*     Title: problem 4                             *           
*    Author: Himanshu Mishra                       *
*     email: himanshu.m786@gmail.com               *
***************************************************/

#include <stdio.h>
#include <stdlib.h>

int input;
int digit[1][6];
int p = 0;
int next_input;
int i;
int j;
int temp = 0;
int max = 0;

int main()  {

	for (i = 100; i < 1000; ++i)  {
		for (j = 100; j < 1000; ++j)  {
		//	printf("product  === %d\n",i*j);
			input = i*j;
			next_input = i*j;
			p = 0;
			while(1) {
				digit[0][p] = next_input % 10;
				next_input = next_input / 10;
				p++;

				if(next_input == 0)  {
						break;
				}

			}
			if((digit[0][0] == digit[0][5]) && (digit[0][1] == digit[0][4]) && (digit[0][2] == digit[0][3]) && (digit[0][3] == digit[0][2]) && (digit[0][4] == digit[0][1]) && (digit[0][5] == digit[0][0]))  {
	//				printf("%d\n", i*j);
					temp = i*j;
					if(temp > max)  {
						max =temp;
						printf("maxium = %d\n", max);
					}
				}
				if(i*j > 1000000)  {
					break;
			

			}
		}
	}

	return 0;
}
