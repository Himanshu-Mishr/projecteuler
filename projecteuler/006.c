#include <stdio.h>
int main()
{
	int i,sq=0,sum=0,b;
/** both are done in same loop ***/
	for(i=1;i<=100;i++)
	{
		sq=sq+(i*i);
		sum=sum+i;
	}
	b=sum*sum;
	printf("\n their difference is %d",b-sq);
	return 0;
}

