/***************************************************
*     Title: probem 44                             *           
*    Author: Himanshu Mishra                       *
*     email: himanshu.m786@gmail.com               *
***************************************************/

#include <stdio.h>
#include <stdlib.h>

#define f(n) (n*(3*n - 1))/2
int penta_num[1][3001];
int sum[1][3001][3001];
int diff[1][3001][3001];
int count = 0;
int main()  {

	for (int i = 1; i < 3001; ++i)
	{
		penta_num[0][i] = f(i);
//		printf("%d pentagonal number is %d\n",i,penta_num[0][i]);

	}
	for (int j = 1; j < 3001; ++j)
	{
		for (int k = 1; k < 3001; ++k)
		{
			sum[0][j][k] = penta_num[0][j] + penta_num[0][k];
//			printf("j = %d  k = %d  sum =  %d\n",j,k,sum[0][j][k]);
		}
	}
	for (int p = 1; p < 3001; ++p)
	{
		for (int q = 1; q < 3001; ++q)
		{
			diff[0][p][q] = penta_num[0][q] - penta_num[0][p];
//			printf("p = %d  q = %d diff = %d\n",p,q,diff[0][p][q]);
		}
	}

	for (int x = 1; x < 3001; ++x)
	{
		for (int y = 1; y < 3001; ++y)
		{
			for (int z = 0; z < 3001; ++z)
			{
			
				if(sum[0][x][y] == penta_num[0][z]) {
					for (int a = 1; a <= z; ++a)
					{
//						printf("%d\n",count);
						if(diff[0][x][y] == penta_num[0][a])  {
							count++;
//							printf("manipulation of %d th element and %d element are pentagonal number",x,y);
							printf("the answer is %d\n", (f(y) - f(x)) );

						}
					}
				}
			}
		}
	}

	return 0;
}
