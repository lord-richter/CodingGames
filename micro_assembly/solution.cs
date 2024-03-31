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
    static Dictionary<string,int> registers = new Dictionary<string,int>();

    static int getSrcImm(string operand) {
        int value = 0;
        if (int.TryParse(operand, out _)) {
            value = Int32.Parse(operand);
        } else {
            string reg = operand.ToLower();
            value = registers[reg];
        }
        Console.Error.WriteLine(">> "+operand+" = "+value);
        return value;
    }

    static void Main(string[] args)
    {

        string[] inputs = Console.ReadLine().Split(' ');
        registers.Add("a",int.Parse(inputs[0]));
        registers.Add("b",int.Parse(inputs[1]));
        registers.Add("c",int.Parse(inputs[2]));
        registers.Add("d",int.Parse(inputs[3]));
        int n = int.Parse(Console.ReadLine());

        string[] program = new string[n];

        for (int i = 0; i < n; i++)
        {
            program[i] = Console.ReadLine();
        }

        int exec = 0;
        while (exec < n) {
            string[] parts = program[exec].Split(" ");

            switch(parts[0].ToUpper())
            {
                case "MOV":
                    string reg = parts[1].ToLower();
                    int value1 = getSrcImm(parts[2]);
                    registers[reg] = value1;
                    exec++;
                    break;
                case "ADD":
                    reg = parts[1].ToLower();
                    value1 = getSrcImm(parts[2]);
                    int value2 = getSrcImm(parts[3]);
                    registers[reg] = value1+value2;
                    exec++;
                    break;                    
                case "SUB":
                    reg = parts[1].ToLower();
                    value1 = getSrcImm(parts[2]);
                    value2 = getSrcImm(parts[3]);
                    registers[reg] = value1-value2;
                    exec++;
                    break;
                case "JNE":
                    int nextexec = Int32.Parse(parts[1]);
                    value1 = getSrcImm(parts[2]);
                    value2 = getSrcImm(parts[3]);
                    if (value1==value2)         
                    { 
                        exec++;
                    } else {
                        exec = nextexec;
                    }        
                    break;
            }

        }

        // Write an answer using Console.WriteLine()
        // To debug: Console.Error.WriteLine("Debug messages...");

        Console.WriteLine(registers["a"]+" "+registers["b"]+" "+registers["c"]+" "+registers["d"]);
    }
}
