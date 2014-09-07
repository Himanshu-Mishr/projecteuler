/****************************************************
*     Title: problem 61                             *           
*    Author: himanshu                         *
*     email: himanshu.m786@gmail.com                   *
****************************************************/

#include <stdio.h>
#include <stdlib.h>
int main()  {
  int x;
  // triangle number 
  printf("\n##### triangle number");
  for (int i = 45; i < 141; ++i)
  {
    x = (i*(i+1))/2;
    printf("\n %d",x);
  }
  // square number
  printf("\n##### square number");
    for (int i = 32; i < 100; ++i)
  {
    x = i*i;
    printf("\n %d",x);
  }
  // pentagonal number
  printf("\n##### pentagonal number");
    for (int i = 26; i < 82; ++i)
  {
    x = (i*(3*i - 1))/2;
    printf("\n %d",x);
  }
  // hexagonal number
  printf("\n##### hexagonal number");
  for (int i = 23; i < 71; ++i)
  {
    x = i*(2*i - 1);
    printf("\n %d",x);
  }
  // heptagonal number
  printf("\n##### heptagonal number");
  for (int i = 21; i < 64; ++i)
  {
    x = (i*(5*i - 3))/2;
    printf("\n %d",x);
  }
  // octogonal number
  printf("\n##### octogonal number");
  for (int i = 19; i < 59; ++i)
  {
    x = i*(3*i - 2);
    printf("\n %d",x);
  }
  return 0;
}

  