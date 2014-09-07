#include<stdio.h>
int main()
{
  long int n,i,s,k;
  printf("\n enter the number:--> ");
  scanf("%ld",&n);
  s=n;
  for(i=1;i<n;i++)
    {
		/**********checking by which number it is divisible ****/
      if(s%i == 0)
	{
		/********** and now printing them **********************/
	  printf("\n%ld",i);
	  /************* the number which divided , is being under check 
	   * whether it is too divisible ***************************/
	  for(k=1;k<i;k++)
	    {
	      if(i%k == 0)
		{
		  printf("i am dividible by %ld ",k);
		}
		/**************and the one which will have be dividible will not
		 * be selected ******************************************/  
	    }
	}
    }
  return 0;
}
