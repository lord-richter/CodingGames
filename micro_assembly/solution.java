import java.util.*;
import java.io.*;
import java.math.*;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Solution {
    static HashMap<String,Integer> registers = new HashMap<String,Integer>();

    private static int getSrcImm(String operand) {
        int value = 0;
        if (!operand.matches("-?\\d+(\\.\\d+)?")) {
            Integer reg = registers.get(operand.toLowerCase());
            if (reg==null) System.err.println("Invalid register:"+operand);
            else value = reg;
        } else {
            value = Integer.valueOf(operand);
        }
        System.err.println(">> "+operand+" = "+value);
        return value;
    }

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        registers.put("a", in.nextInt());  // register initial value
        registers.put("b", in.nextInt());  // register initial value
        registers.put("c", in.nextInt());  // register initial value
        registers.put("d", in.nextInt());  // register initial value
        int n = in.nextInt();  // number of instructions
        // eat input
        if (in.hasNextLine()) {
            in.nextLine();
        }
        // get N instructions and process as they arrive
        ArrayList<String> program = new ArrayList<String>();
        for (int i = 0; i < n; i++) {
            String instruction = in.nextLine();
            program.add(i,instruction);
        }

        int exec = 0;
        while (exec<program.size()) {
            String[] parts = program.get(exec).split(" ");
            switch (parts[0].toUpperCase()) {
                case "MOV":
                    int value = getSrcImm(parts[2]);
                    registers.put(parts[1].toLowerCase(), value);
                    exec++;
                    break;
                case "ADD":
                    int value1 = getSrcImm(parts[2]);
                    int value2 = getSrcImm(parts[3]);
                    registers.put(parts[1].toLowerCase(), value1+value2);
                    exec++;
                    break;
                case "SUB":
                    value1 = getSrcImm(parts[2]);
                    value2 = getSrcImm(parts[3]);
                    registers.put(parts[1].toLowerCase(), value1-value2);
                    exec++;
                    break;
                case "JNE":
                    int exec1 = getSrcImm(parts[1]);
                    value1 = getSrcImm(parts[2]);
                    value2 = getSrcImm(parts[3]);
                    if (value1==value2) exec++;
                    else exec=exec1;
                    break;
                default:
                    System.err.println("OOPS!");
                    break;

            }
        }


        // Write an answer using System.out.println()
        // To debug: System.err.println("Debug messages...");

        String answer = "";
        for (String register : registers.keySet()) {
            answer = answer + registers.get(register) + " ";
        }
        System.out.println(answer.trim());
    }
}
