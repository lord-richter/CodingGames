import java.util.*;
import java.io.*;
import java.math.*;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 * ---
 * Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.
 **/
class Player {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int lightX = in.nextInt(); // the X position of the light of power
        int lightY = in.nextInt(); // the Y position of the light of power
        int initialTx = in.nextInt(); // Thor's starting X position
        int initialTy = in.nextInt(); // Thor's starting Y position
        int currentTy = initialTy;
        int currentTx = initialTx;

        // game loop
        while (true) {
            int remainingTurns = in.nextInt(); // The remaining amount of turns Thor can move. Do not remove this line.

            // clear direction for each loop
            String direction = "";

            // Assign N and S first, to build proper string
            // If directly N or S, then this gets skipped
            // update the current location
            // bounds check to ensure staying within the area
            if (lightY>currentTy) {
                direction = direction + "S";
                currentTy = Integer.min(39,currentTy + 1);
            } else if (lightY<currentTy) {
                direction = direction + "N";
                currentTy = Integer.max(0,currentTy - 1);
            }

            // Assign E and W second, to build proper string
            // If directly E or W, then this gets skipped
            if (lightX>currentTx) {
                direction = direction + "E";
                currentTx = Integer.min(17,currentTx+1);
            } else if (lightX<currentTx) {
                direction = direction + "W";
                currentTx = Integer.max(0,currentTx+1);
            }

            // Write an action using Console.WriteLine()
            // To debug: Console.Error.WriteLine("Debug messages...");


            // A single line providing the move to be made: N NE E SE S SW W or NW
            System.out.println(direction);
        }
    }
}
