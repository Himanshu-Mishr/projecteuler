/*****************************************************************
*     Title: version 2 of problem 69                             *           
*    Author: hm                                      *
*     email: himanshu.m786@gmail.com                                *
*****************************************************************/

#include <stdio.h>
#include <stdlib.h>


int main()  {
  int i=0,j=0,c=0;
  float x=0,k;
  int count = 0;
  float max = 0;
  float max_temp = 0;
  int max_number = 0;

  for (i = 1; i <= 1000000; ++i)
  { 
    x = 1;
    count = 0;
    for (j = 1; j < i; ++j)
    {
      if (i%j == 0)
      {
        for ( c = 2 ; c <= j ; c++ )
        {
          if ( j%c == 0 )
          {
            break;
          }
        }
        if ( c == j )
        { 
          count++;
          x = x * (j-1)/j;
        }

      }
      
      }
      if(count == 0) {
        for(k = 2; k < i; ++k)
        {
          x = x * (k-1)/k;
        }
        max_temp = (i*1.0)*x;
      }
      if(count != 0) {
        max_temp = i/((i*1.0)*x);
      }

    if(max < max_temp) {
      max = max_temp;
      max_number = i;
    }  
    }
  printf("\n answer max_number = %d  max = %f",max_number,max);
  return 0;      
  }

        //y = j;
        //x = j;
        //flag = 0;
/*        while(x>1) 
        {
          if(y%x == 0) 
          {
            flag = 0;
            break;
          }
          flag = 1;
          x--;
        }
        printf("\n flag == %d",flag);
        if(flag == 1) 
        {
        printf(" \n prime --->  %d ",j);
        }*/
//      }
//    }
/**    
    // taking the truth out
    printf("\n actual array contains -> ");

    for (int l = 0; l < count_for_array; ++l)
    {
      printf(" %d ",divisibleArray[l]);
    }
*/    
 /*   
    // child loop for finding prime from divisibleArray
    printf("\n from it prime =  ");
    for (k = 0; k < count_for_array + 1; ++k)
    {
      y = divisibleArray[k];
      //printf("\n y = %d",y);
      x = y/2;
      flag = 0;
      while(x>1) {
        printf("\n y =  %d  x = %d ",y,x);
        if(y%x == 0) {
          flag = 0;
          break;
        }
        else {
          flag = 1;
        }
        x--;
      }
      if(flag == 1) {
        printf(" --->  %d ",y);
      }
    }*/
//  }
//  return 0;
//}
