#include <stdio.h>

bool checkPrime(long long int n) {
  int flag = 0;
  for (int i = 2; i < n/2; ++i)
  {
    if(n%i == 0) {
      return false;
    }
    flag = 1;
  }
  if(flag == 1) {
    return true;
  }
  return true;
}


int main() {


  int real_count = -1, prime_count = -2;
  long long int sum = 0, counter = -1, x,y;
  float per = 0.0;

  for (int n = 1; n < 30001; ++n)  {
/*even*/
    if(n%2 == 0)  {
      x = (n*n) + 1;
      real_count++;
      y = (n*n) + 1 + n;
      real_count++;

  /*check Prime ? */
      // x ---------------------
      if(checkPrime(x))   {
        prime_count++;
      }
      // y ---------------------
      if(checkPrime(y))   {
        prime_count++;
      }
    }

/*odd*/
    else {
      counter++;
      x = n*n;
      real_count++;
      y = (n*n - 6*counter);
      real_count++;

  /*check Prime ? */

      // x-------------------
      if(checkPrime(x))   {
        prime_count++;
      }

      // y--------------------
      if(checkPrime(y))   {
        prime_count++;
      }

    }


    per = 0.0;
    per = ((float)prime_count)/((float) real_count) * 100.0;
    printf("\n%f", per);
    if(per < 10) {
      printf("\nYUP this is the answer..... lenght = %d ",n);
    }
  }

}
