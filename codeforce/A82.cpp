// coder         : Himanshu Mishra (himanshu.m786@gmail.com)
// about program : A82

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <numeric>
#include <cstdlib>

using std::cin;
using std::cout;
using std::endl;
using std::string;
using std::vector;
using namespace std;

int main() {

    int x, temp;
    cin >> x;


    //string a = "Sheldon", b = "Leonard", c = "Penny", d = "Rajesh", e = "Howard";

    vector<int> v;
    //v = {"a", "b", "c", "d", "e"};
    v.push_back(1);
    v.push_back(2);
    v.push_back(3);
    v.push_back(4);
    v.push_back(5);

    for (int i = 0; i < x; ++i)
    {
        temp = v[i];
        v.push_back(temp);v.push_back(temp);
    }

    if (temp == 1) {
        cout << "Sheldon" << endl;
    }
    else {
        if (temp == 2) {
        cout << "Leonard" << endl;
        }
        else {
            if (temp == 3) {
                cout << "Penny" << endl;
            }
            else {
                if (temp == 4) {
                    cout << "Rajesh" << endl;
                }
                else {
                    cout << "Howard" << endl;
                }
            }
        }
    }
}
