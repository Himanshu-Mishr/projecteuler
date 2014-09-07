/*=============================================================================
 | Program Name:  name
 |
 |  Description:
 |
 +-----------------------------------------------------------------------------
 |       Author: Himanshu Mishra
 |       Email : himanshu.m786@gmail.com
 *===========================================================================*/

#include <stdio.h>
#include <stdlib.h>


int main() {
    long long int x = 75, y=0, p=175, q=0;
    for (long long i = 1; i < 10000000001; ++i)  {
        y = x + 20;
        q = p + 30;
        printf("%lld = %lld\n", x, p);
        x = y;
        p = q;
    }

    return 0;
}
