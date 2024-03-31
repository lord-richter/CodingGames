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
        int charW = int.Parse(Console.ReadLine());
        int charH = int.Parse(Console.ReadLine());
        string message = Console.ReadLine();
        string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ?";
        for (int i = 0; i < charH; i++)
        {
            string asciiRow = Console.ReadLine();
            foreach (char c in message.ToUpper())
            {
                int index = alphabet.IndexOf(c);
                if (index<0) index=26;
                string part = asciiRow.Substring(index*charW,Math.Min(charW,asciiRow.Length-(index*charW)));
                Console.Write(part);
            }
            Console.WriteLine();
        }

        // Write an answer using Console.WriteLine()
        // To debug: Console.Error.WriteLine("Debug messages...");
        
    }
}
