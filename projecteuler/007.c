#include<stdio.h>
int main()
{
  int i,j,a,flag,s=0;
  for(i=2;i<=999999;i++)
    {
      flag=0;
      for(j=2;j<i;j++) 
	{
	  a=i%j;
	  if(a==0) 
	    flag=1;
	}
      if(flag==1) 
	printf("%d is not prime\n", i);
      else 
      {
		  s=s+1;
	printf("%d is prime and counter number is %d \n", i,s);
/******* i wanted s=10001 so checked it from output .. 
         but i think that we can use break statement 
	 here to get out from the loop at s=10001 *******/   
}	
    }
  return 0;
}