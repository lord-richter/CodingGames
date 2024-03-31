import java.util.*;
import java.io.*;
import java.math.*;
import java.util.ArrayList;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Solution {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int charW = in.nextInt(); // ascii art character width
        int charH = in.nextInt(); // ascii art character height
        // apparently eats the next line
        if (in.hasNextLine()) {
            in.nextLine();
        }
        // gets the message
        String message = in.nextLine();
        //System.err.println(message);
        // get the ascii art
        String alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ?";
        for (int i = 0; i < charH; i++) {
            String asciiRow = in.nextLine();
            //System.err.println("["+asciiRow+"]"+asciiRow.length());
            // loop over each letter and output the ascii art from this row
            for (int c = 0;c < message.length();c++) {
                int index = alphabet.indexOf(message.toUpperCase().charAt(c));
                if (index<0) { index=26; }
                String part = asciiRow.substring(index*charW, Math.min(asciiRow.length(),(index*charW)+charW));
                System.out.print(part);
            }
            System.out.println("");
        }



        // Write an answer using System.out.println()
        // To debug: System.err.println("Debug messages...");

    }
}
