#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 * ---
 * Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.
 **/

int main()
{
    // the X position of the light of power
    int light_x;
    // the Y position of the light of power
    int light_y;
    // Thor's starting X position
    int initial_tx;
    // Thor's starting Y position
    int initial_ty;
    // Thor's current postion
    int current_tx,current_ty;

    scanf("%d%d%d%d", &light_x, &light_y, &initial_tx, &initial_ty);

    current_tx = initial_tx;
    current_ty = initial_ty;
    
    char direction[3];

    // game loop
    while (1) {
        // The remaining amount of turns Thor can move. Do not remove this line.
        int remaining_turns;
        scanf("%d", &remaining_turns);

        // clear direction for each loop
        strcpy(direction,"");


        // Assign N and S first, to build proper string
        // If directly N or S, then this gets skipped
        // update the current location
        // bounds check to ensure staying within the area
        if (light_y>current_ty) {
            strcat(direction,"S");
            current_ty = current_ty + 1;
        } else if (light_y<current_ty) {
            strcat(direction,"N");
            current_ty = current_ty - 1;
        }

        // Assign E and W second, to build proper string
        // If directly E or W, then this gets skipped
        if (light_x>current_tx) {
            strcat(direction,"E");
            current_tx = current_tx + 1;
        } else if (light_x<current_tx) {
            strcat(direction,"W");
            current_tx = current_tx + 1;
        }

        // Write an action using printf(). DON'T FORGET THE TRAILING \n
        // To debug: fprintf(stderr, "Debug messages...\n");


        // A single line providing the move to be made: N NE E SE S SW W or NW
        printf("%s\n",direction);
    }

    return 0;
}
