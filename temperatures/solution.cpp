#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

int main()
{
    int n; // the number of temperatures to analyse
    int closest=5527;
    cin >> n; cin.ignore();
    for (int i = 0; i < n; i++) {
        int t; // a temperature expressed as an integer ranging from -273 to 5526
        cin >> t; cin.ignore();

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

    // Write an answer using cout. DON'T FORGET THE "<< endl"
    // To debug: cerr << "Debug messages..." << endl;

    cout << closest << endl;
}
