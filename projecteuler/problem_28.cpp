#include <iostream>
#include "Timer.h"
using namespace std;
int main() {
  Timer timer = Timer();
  timer.start();

  int sum = 0;
  int counter = -1;
  for (int n = 1; n < 6; ++n)
  {
    /*even*/
    if(n%2 == 0)  {
      int x,y;
      x = (n*n) + 1;
      y = (n*n) + 1 + n;
      sum = sum + x;
      sum = sum + y;
    }
    /*odd*/
    else {
      counter++;
      int x,y;
      x = n*n;
      y = (n*n - 6*counter);
      sum = sum + x;
      sum = sum + y;
    }
  }
  cout<< "sum = " << sum-1 << endl;

  double duration = timer.stop();
  timer.printTime(duration);
}
