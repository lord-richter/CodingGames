#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 * ---
 * Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.
 **/

int main()
{
    int light_x; // the X position of the light of power
    int light_y; // the Y position of the light of power
    int initial_tx; // Thor's starting X position
    int initial_ty; // Thor's starting Y position
    cin >> light_x >> light_y >> initial_tx >> initial_ty; cin.ignore();

    string direction("");

    int current_tx = initial_tx;
    int current_ty = initial_ty;


    // game loop
    while (1) {
        int remaining_turns; // The remaining amount of turns Thor can move. Do not remove this line.
        cin >> remaining_turns; cin.ignore();

        // clear direction for each loop
        direction = "";


        // Assign N and S first, to build proper string
        // If directly N or S, then this gets skipped
        // update the current location
        // bounds check to ensure staying within the area
        if (light_y>current_ty) {
            direction = direction + "S";
            current_ty = current_ty + 1;
        } else if (light_y<current_ty) {
            direction = direction + "N";
            current_ty = current_ty - 1;
        }

        // Assign E and W second, to build proper string
        // If directly E or W, then this gets skipped
        if (light_x>current_tx) {
            direction = direction + "E";
            current_tx = current_tx + 1;
        } else if (light_x<current_tx) {
            direction = direction + "W";
            current_tx = current_tx + 1;
        }

        // Write an action using cout. DON'T FORGET THE "<< endl"
        // To debug: cerr << "Debug messages..." << endl;


        // A single line providing the move to be made: N NE E SE S SW W or NW
        cout << direction << endl;
    }
}
