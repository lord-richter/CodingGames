import java.util.*;
import java.io.*;
import java.math.*;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Solution {


    public static void main(String args[]) {
        int closest = 5527; // the closest to zero, initially out of bounds


        Scanner in = new Scanner(System.in);
        int n = in.nextInt(); // the number of temperatures to analyse
        for (int i = 0; i < n; i++) {
            int t = in.nextInt(); // a temperature expressed as an integer ranging from -273 to 5526

            // if the absolute temp is lower than closest, new candidate
            if (Math.abs(t) < Math.abs(closest)) {
                closest = t;
            //if the absolute temp is equal to closest, only take positive temps
            } else if ((Math.abs(t) == Math.abs(closest)) && t>0) {
                closest = t;
            }

        }

        if (n == 0) {
            closest = 0;
        }

        // Write an answer using System.out.println()
        // To debug: System.err.println("Debug messages...");

        System.out.println(closest);
    }
}
