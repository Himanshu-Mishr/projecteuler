/*=============================================================================
 | Program Name:  problem100
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
    for (int i=10; i < 1000000000000; ++i)  {
            int count = (int) (2/3)*i;
            printf("\n%d__>%d",i, count);
            for (int j = count; j < i; ++j)  {
                if(i^2 - j^2 - i + 2*j == 0)  {
                    // printf("\n %d______>  %d",i, j);
                }
            }
        }
    return 0;
}

