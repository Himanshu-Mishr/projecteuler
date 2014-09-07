// coder         : Himanshu Mishra (himanshu.m786@gmail.com)
// about program : problem 124

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <numeric>
#include <cstdlib>
#include <cmath>

using std::cin;
using std::cout;
using std::endl;
using std::string;
using std::vector;
using namespace std;

int main() {

    for (int i = 0; i < 18; ++i) // 2
    {
        for (int j = 0; j < 12; ++j) // 3
        {
            for (int k = 0; k < 9; ++k) //5
            {
                for (int l = 0; l < 7; ++l) // 7
                {
                    for (int m = 0; m < 6; ++m) // 11
                    {
                        for (int n = 0; n < 6; ++n) // 13
                        {
                            for (int o = 0; o < 6; ++o) // 17
                            {
                                cout << " >> " << pow(2, i) * pow(3, j) * pow(5, k) * pow(7, l) * pow(11, m)  * pow(13, n)  * pow(17, o) << endl;
                            }
                        }
                    }
                }
            }
        }
    }
    cout << "=======the end==========" << endl;
}
