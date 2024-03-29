#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

int main()
{
    // the number of temperatures to analyse
    int n;
    int closest = 5527;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        // a temperature expressed as an integer ranging from -273 to 5526
        int t;
        scanf("%d", &t);

        // if the absolute temp is lower than closest, new candidate
        if (abs(t) < abs(closest)) {
            closest = t;
        //if the absolute temp is equal to closest, only take positive temps
        } else if ((abs(t) == abs(closest)) && t>0) {
            closest = t;
        }
    }

    if (n==0) {
        closest = 0;
    }
    // Write an answer using printf(). DON'T FORGET THE TRAILING \n
    // To debug: fprintf(stderr, "Debug messages...\n");

    printf("%d\n",closest);

    return 0;
}
