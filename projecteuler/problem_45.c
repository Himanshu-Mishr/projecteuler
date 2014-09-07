/****************************************************
*     Title: problem 45                             *           
*    Author: Himanshu Mishra                        *
*     email: himanshu.m786@gmail.com                *
****************************************************/

#include <stdio.h>
#include <stdlib.h>

#define t(n) (n*(n+1))/2 
#define p(n) (n*(3*n-1))/2
#define h(n) (n*(2*n-1))

long long int tri[1][26640],penta[1][26640],hexa[1][26640];

int main()  {

	for (int i = 1; i < 26640; ++i)
	{
		tri[0][i] = t(i);
		penta[0][i] = p(i);
		hexa[0][i] = h(i);
		printf("%d th term tri = %lld || penta = %lld || hexa = %lld\n",i,tri[0][i],penta[0][i],hexa[0][i]);
	}
	for (int p = 1; p < 26640; ++p)
	{
		for (int q = 1; q < 26640; ++q)
		{
			if(tri[0][p] == penta[0][q])  {
				for (int r = 1; r < 26640; ++r)
				{
					if(penta[0][q] == hexa[0][r])  {
						printf("%lld\n",tri[0][p]);
					}
				}
			}
		}
	}

	return 0;
}
