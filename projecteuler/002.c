/********************************
problem written by std_win
********************************/
#include<stdio.h>
int main()  {
  int i,x=1,y=0,z=0,s=0;
  for(i=1;i<=40;i++)
    /********* just took 40 like this .. no problem ..*********/
    {
      y = x + z;
      z=x;
      x=y;    
      printf("\n%d",y);
      /****************
        to restrict the number above 4000000
      */
       if(y<4000000)
	 {
	 /************
         to restrict the odds and pass the evens
	 */    
	  if(y%2==0)
	    {
	      s=y+s;
	      printf("\n i am here %d",s);
	    }
	 }
    }     
  printf("\nthe sum is %d\n",s);
  return 0;
}
