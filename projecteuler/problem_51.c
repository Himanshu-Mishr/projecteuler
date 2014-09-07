/*=============================================================================
 | Program Name:  recursion
 |
 |  Description:  recursion babe
 |
 +-----------------------------------------------------------------------------
 |       Author: Himanshu Mishra
 |       Email : himanshu.m786@gmail.com
 *===========================================================================*/

#include <stdio.h>

int recursion(int , int);
long long int count = 0;

int main() {
    for (int i = 1; i < 21; ++i)
    {
        printf("---------------------------------\n");
        recursion(i, i);
        printf("Total count for %d : %lld\n", i, count);
        count = 0;
    }
    return 0;
}

int recursion(int x, int y)  {
    if (x == 0 || y == 0) {
        count ++;
    }
    if (x > 0 && y > 0) {

    }
    else {
        return 0;
    }
    recursion(x-1, y);
    recursion(x, y-1);
}

/*
 ⚙  ~/w/competition   master ±  ./recur_c_version    Sat Feb  8 16:34:10 IST 2014
---------------------------------
Total count for 1 : 2
---------------------------------
Total count for 2 : 6
---------------------------------
Total count for 3 : 20
---------------------------------
Total count for 4 : 70
---------------------------------
Total count for 5 : 252
---------------------------------
Total count for 6 : 924
---------------------------------
Total count for 7 : 3432
---------------------------------
Total count for 8 : 12870
---------------------------------
Total count for 9 : 48620
---------------------------------
Total count for 10 : 184756
---------------------------------
Total count for 11 : 705432
---------------------------------
Total count for 12 : 2704156
---------------------------------
Total count for 13 : 10400600
---------------------------------
Total count for 14 : 40116600
---------------------------------
Total count for 15 : 155117520
---------------------------------
Total count for 16 : 601080390
---------------------------------
Total count for 17 : 2333606220
---------------------------------
Total count for 18 : 9075135300
---------------------------------
Total count for 19 : 35345263800
---------------------------------
Total count for 20 : 137846528820
 */
