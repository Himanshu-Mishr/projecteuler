/*=============================================================================
 | Program Name:  prime
 |
 |  Description:  prime
 |
 +-----------------------------------------------------------------------------
 |       Author: Himanshu Mishra
 |       Email : himanshu.m786@gmail.com
 *===========================================================================*/

#include <stdio.h>
#include <stdlib.h>


int main() {
    int x, flag=0;
    for (int i = 1; i < 100000; i += 2)  {
        x = (int) i/2;
        while(x>2) {
            if (i%x == 0) {
                printf("caught >>>%d\n", i);
                flag = 0;
                break;
            }
            flag = 1;
        }
        if (flag == 1)
            printf("--> %d\n", i);

    }
    return 0;
}
