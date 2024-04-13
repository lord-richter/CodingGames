import java.util.*;
import java.io.*;
import java.math.*;
import java.lang.StringBuilder;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Solution {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        String typedKeys = in.nextLine();

        int cursor = 0;     // where the next character goes
        String output = ""; // store the output as each character processed

        System.err.println("["+typedKeys+"] "+typedKeys.length());

        // loop over all character in the input string
        for (int i = 0; i<typedKeys.length();i++) {
            char cin = typedKeys.charAt(i);
            System.err.print("["+cin+"] ");

            // cursor left
            if (cin=='<') {
                // back up one, but do not go past beginning
                cursor = Math.max(0,cursor-1);
            // cursor right    
            } else if (cin=='>') {
                // forward one, but do not go past end
                cursor = Math.min(cursor+1,output.length());

            // backspace
            } else if (cin=='-') {
                // make sure we are not backing too far
                if (cursor>0) {
                    cursor--;
                    output = new StringBuilder(output).deleteCharAt(cursor).toString();
                }
            // not a cursor movement character    
            } else {
                // handle insert in middle vs append to end 
                // to avoid out of bounds.
                if (cursor<output.length()) {
                    output = new StringBuilder(output).insert(cursor, cin).toString();
                } else {
                    output = output + cin;
                }
                cursor = cursor + 1;
            }
            System.err.print("("+cursor+") ");
            System.err.println("'"+output+"'");
        }

        // Write an answer using System.out.println()
        // To debug: System.err.println("Debug messages...");

        System.out.println(output);
    }
}
