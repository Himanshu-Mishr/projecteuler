#include <iostream>
using namespace std;

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


  int real_count = -1;
  int prime_count = -2;
  long long int sum = 0;
  long long int counter = -1;

  for (int n = 1; n < 20001; ++n)  {
/*even*/
    if(n%2 == 0)  {
      long long int x,y;
      x = (n*n) + 1;
      real_count++;
      y = (n*n) + 1 + n;
      real_count++;

  /*check Prime ? */
      // x ---------------------
      if(checkPrime(x))
      {
        //cout << " even " << " x is prime " << x << endl;
        prime_count++;
      }
      else {
        //cout << " even " << " x is Not prime " << x << endl;
      }
      // y ---------------------
      if(checkPrime(y)){
        prime_count++;
        //cout << " even " << " y is prime " << y << endl;
      }
      else {
        //cout << " even " << " y is Not prime " << y << endl;
        }
      }

/*odd*/
    else {
      counter++;
      long long int x,y;
      x = n*n;
      real_count++;
      y = (n*n - 6*counter);
      real_count++;

  /*check Prime ? */

      // x-------------------
      if(checkPrime(x)) {
        prime_count++;
        //cout << " odd " << " x is prime " << x << endl;
      }
      else {
        //cout << " odd " << " x is Not prime " << x << endl;
      }

      // y--------------------
      if(checkPrime(y)){
        prime_count++;
        //cout << " odd " << " y is prime " << y << endl;
      }
      else {
        //cout << " odd " << " y is Not prime " << y << endl;
      }
    }


    float per = 0.0;
    per = ((float)prime_count)/((float) real_count) * 100.0;
    //cout << "Lenght = " << n << endl;
    //cout << "Real count = " << real_count << endl;
    //cout << "Prime Count = " << prime_count << endl;
    cout << per << endl;
    //cout << "--------------------------------------" << endl;
    if(per < 10) {
      cout << "YUP this is the answer " << "lenght =  " << n << endl;
    }
  }

}
