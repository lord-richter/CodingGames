using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Solution
{
    static void Main(string[] args)
    {
        int closest = 5527; // the closest to zero, initially out of bounds
        int n = int.Parse(Console.ReadLine()); // the number of temperatures to analyse
        string[] inputs = Console.ReadLine().Split(' ');
        for (int i = 0; i < n; i++)
        {
            int t = int.Parse(inputs[i]);// a temperature expressed as an integer ranging from -273 to 5526

                        // if the absolute temp is lower than closest, new candidate
            if (Math.Abs(t) < Math.Abs(closest)) {
                closest = t;
            //if the absolute temp is equal to closest, only take positive temps
            } else if ((Math.Abs(t) == Math.Abs(closest)) && t>0) {
                closest = t;
            }
        }

        if (n == 0) {
            closest = 0;
        }

        // Write an answer using Console.WriteLine()
        // To debug: Console.Error.WriteLine("Debug messages...");

        Console.WriteLine(closest);
    }
}
