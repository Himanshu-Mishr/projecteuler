#include<stdio.h>
int main()
{
  int i,j,a,flag,s=0;
  long long int k=0;
  for(i=2;i<=2000000;i++)
    {
      flag=0;
      for(j=2;j<i;j++) 
	{
	  a=i%j;
	  if(a==0) 
	    flag=1;
	}
      if(flag==1) 
	printf(" ");
      else 
      {
		  s=s+1;
		  k = k + i;
	printf("\n || %d |||| %d |||| %lld ||", i,s,k);
/******* i wanted s=10001 so checked it from output .. 
         but i think that we can use break statement 
	 here to get out from the loop at s=10001 *******/   
}	
    }
  return 0;
}
