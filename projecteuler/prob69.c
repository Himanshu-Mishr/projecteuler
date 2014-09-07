/**************************************************
*     Title: prob69.c                             *           
*    Author: himanshu mishra                       *
*     email: himanshu.m786@gmail.com                 *
**************************************************/

#include <stdio.h>
#include <stdlib.h>
// we will be using pointer to transfer the value.
int counter, *counter_ptr = &counter;
//you do your working with counter and when you have to pass the value then get the address
//means dereference from it

// (dividend) = (divisor)    X   (quotient)   +    remainder
//     |               |                               |                        
// big number   smaller number             next number to be proccessd

// this function just has to checks when the gcd is 1.
int gcd(int dividend,int divisor) {
  int temp = 0;
  //const int x = dividend;
  //const int y = divisor;
  temp = dividend%divisor;
  if(divisor == 1 && temp == 1) {
      return 0;
    }
  if(temp == 0)  {
    return 1;
    //printf(" =  %d",divisor);

  }
  else
  {
    gcd(divisor,temp);
  }

  //printf("\n dividend = %d divisor = %d output = %d reaminder = %d",dividend,divisor,dividend/divisor,dividend%divisor);
  return 0;
}

int main()  {
  int count;
  for (int i = 2; i < 100; ++i)
  {
    //  if the input i in itself prime
    prime_checker(i);
    /*//printf("\n -------> %d",i);
    count = 0;
    for (int j = 1; j < i; ++j)
    { dividend = i;
      divisor = j;
      remainder = 0;
      //  i want print out of what is going in here ...
      while(1) {
        remainder = dividend%divisor;
        printf("\n   dividend = %d  |  divisor = %d quotient = %d reaminder = %d",dividend,divisor,dividend/divisor,remainder);
        if(remainder == 0){
          count++;
          break;
        }
        dividend = divisor;
        divisor = remainder;

      }
      printf("\ngcd(%d,%d) = %d",i,j,divisor);
    }
    printf("\n i = %d  count = %d",i,count); */
  }
  return 0;
}
