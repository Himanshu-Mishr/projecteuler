/****************************************************
*     Title: problem 75                             *           
*    Author: himanshu mishra                        *
*     email: himanshu.m786@gmail.com                *
****************************************************/

#include <stdio.h>
#include <stdlib.h>

int main()  {
  int length,m,n;
  for ( m = 1; m < 1300; ++m)
   {
     for ( n = 1; n < 75100; ++n)
     {
        if(m>n) {
          length = 2*(m*m + m*n);
          if (length < 1500000) {
            printf("%d, \n",length);
          }
        }
      }
   }
  return 0;
}
