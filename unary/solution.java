import java.util.*;
import java.io.*;
import java.math.*;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Solution {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        String message = in.nextLine();

        System.err.println("Debug: "+message);
        
        String binary = "";
        String encoded = "";

        for (int i=0;i<message.length();i++) {
            int ascii = (int) message.charAt(i);
            binary = binary + String.format("%7s",Integer.toBinaryString(ascii)).replace(" ","0");  
        }

        System.err.println("Debug: "+binary);

        char bit = binary.charAt(0); 
        int run = 1;
        String block1,block2;
        for (int c=1;c<binary.length();c++) {
            if (binary.charAt(c)==bit) {
                run++;
            } else {
                block1 = (bit=='1'?"0":"00")+" ";
                block2 = "0".repeat(run)+" ";
                bit = binary.charAt(c);
                run=1;
                encoded = encoded + block1 + block2;
            }
        }
        block1 = (bit=='1'?"0":"00")+" ";
        block2 = "0".repeat(run);
        encoded = encoded + block1 + block2;


        // Write an answer using System.out.println()
        // To debug: System.err.println("Debug messages...");

        System.out.println(encoded);
    }
}