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
        string typedKeys = Console.ReadLine();

        // where next character goes
        int cursor = 0; 

        // running output
        string output = "";

        for (int i=0;i<typedKeys.Length;i++)
        {
            string cin = typedKeys.Substring(i,1);
            Console.Error.Write("["+cin+"] ");
            
            if (cin=="<")  // cursor left
            {
                // prevent going past left bounds
                cursor = Math.Max(0,cursor-1);
            } else if (cin==">") // cursor right
            {
                // prevent going past right bounds
                cursor = Math.Min(cursor+1,output.Length);
            } else if (cin=="-")
            {
                // prevent going past left bounds
                if (cursor>0)
                {
                    cursor--;
                    output = output.Remove(cursor,1);
                }
            } else 
            {
                // handle cases where cursor in middle
                // and at the end
                if (cursor<output.Length) // in the middle
                {
                    output = output.Insert(cursor,cin);
                } else { // end of string
                    output = output + cin;
                }
                cursor++;
            }

            Console.Error.Write("(" + cursor + ") ");       
            Console.Error.WriteLine(output);
        }

        // Write an answer using Console.WriteLine()
        // To debug: Console.Error.WriteLine("Debug messages...");

        Console.WriteLine(output);
    }
}
