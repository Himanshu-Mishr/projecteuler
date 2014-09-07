#include<stdio.h>
int main()  {
  int i,s=0;
 for(i=1;i<1000;i++)  {
   /*************** right now for i giving me input one by one as 
                    1,2,3.... . so i have to bar it first so that 
                    i get only multiple of 3 as well as 5  ***********
   *****************/
    if(i%3==0 || i%5==0)
        {
	   s =s + i;
	   printf("\n%d is added, we get %d",i,s);
	}
   
 }
 printf("\n the sum is %d \n ",s);
 return 0;
}

