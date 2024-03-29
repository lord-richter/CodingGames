using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;


/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 * ---
 * Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.
 **/
class Player
{
    static void Main(string[] args)
    {
        string[] inputs = Console.ReadLine().Split(' ');
        int lightX = int.Parse(inputs[0]); // the X position of the light of power
        int lightY = int.Parse(inputs[1]); // the Y position of the light of power
        int initialTx = int.Parse(inputs[2]); // Thor's starting X position
        int initialTy = int.Parse(inputs[3]); // Thor's starting Y position
        int currentTx = initialTx; // Thor's current location X
        int currentTy = initialTy; // Thor's current location Y

        // game loop
        while (true)
        {
            int remainingTurns = int.Parse(Console.ReadLine()); // The remaining amount of turns Thor can move. Do not remove this line.


            // clear direction for each loop
            String direction = "";

            // Assign N and S first, to build proper string
            // If directly N or S, then this gets skipped
            // update the current location
            // bounds check to ensure staying within the area
            if (lightY>currentTy) {
                direction = direction + "S";
                currentTy = Math.Min(39,currentTy + 1);
            } else if (lightY<currentTy) {
                direction = direction + "N";
                currentTy = Math.Max(0,currentTy - 1);
            }

            // Assign E and W second, to build proper string
            // If directly E or W, then this gets skipped
            if (lightX>currentTx) {
                direction = direction + "E";
                currentTx = Math.Min(17,currentTx+1);
            } else if (lightX<currentTx) {
                direction = direction + "W";
                currentTx = Math.Max(0,currentTx+1);
            }

            // Write an action using Console.WriteLine()
            // To debug: Console.Error.WriteLine("Debug messages...");


            // A single line providing the move to be made: N NE E SE S SW W or NW
            Console.WriteLine(direction);
        }
    }
}
