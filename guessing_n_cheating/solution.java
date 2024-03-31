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
        int rounds = in.nextInt();
        // eat input line
        if (in.hasNextLine()) {
            in.nextLine();
        }

        int cheatround = 0;
        int guesslower = 0;
        int guessupper = 101;
        HashMap<Integer,String> previous = new HashMap<Integer,String>();

        for (int round = 0; round < rounds; round++) {
            String line = in.nextLine();
            Integer guess = Integer.valueOf(line.substring(0, line.indexOf(" ")).trim());
            String answer = line.substring(line.indexOf(" ")).trim();
            System.err.println("Round: "+round+" >> Bob:"+guess+" >> Alice:"+answer);


            // bob is an idiot
            if (cheatround==0) {
                if (guess<guesslower || guess>guessupper) {
                    System.err.println(">> Bob is an idiot");
                }

                // easy case, alice sends bob out of bounds
                if ((guess>=100 && answer.contains("low")) || (guess<=1 && answer.contains("high"))) {
                    System.err.println(">> Going out of range");
                    cheatround=round+1;
                    System.out.println("Alice cheated in round "+cheatround);                  
                } 
                // bob guesses at edge of range and gets pushed to range edge
                else if ((guess<=guesslower && answer.contains("high")) || (guess>=guessupper && answer.contains("low"))) {
                    System.err.println(">> Going wrong direction");
                    cheatround=round+1;
                    System.out.println("Alice cheated in round "+cheatround);
                }
                // bob guesses and gets pointed outside of bounds
                else if ((guess==guesslower+1 && answer.contains("high")) || (guess==guessupper-1 && answer.contains("low"))) {
                    System.err.println(">> Going to a boundry");
                    cheatround=round+1;
                    System.out.println("Alice cheated in round "+cheatround);
                }
                // out of bounds right answer
                else if ((guess<guesslower || guess>guessupper) && answer.contains("right")) {
                    System.err.println(">> Correct answer was out of bounds");
                    cheatround=round+1;
                    System.out.println("Alice cheated in round "+cheatround);
                }
                // alice gave different answers to same guess
                else if (previous.containsKey(guess) && previous.get(guess).compareTo(answer)!=0) {
                    System.err.println(">> Different answer to same guess");
                    cheatround=round+1;
                    System.out.println("Alice cheated in round "+cheatround);
                }
                // no cheating detected
                else {
                    if (answer.contains("right")) {
                        System.err.println(">> Correct answer was given");
                    } else {
                        System.err.println(">> No cheating detected, establish new bounds");
                        // set new upper and lower bounds
                        guessupper = (answer.contains("high") ? Math.min(Math.min(101,guessupper),guess): guessupper);
                        guesslower = (answer.contains("low") ? Math.max(Math.max(0,guesslower),guess) : guesslower);
                        System.err.println("Range >> "+guesslower+" to "+guessupper);
                        previous.put(guess,answer);
 
                        // but wait! nowhere to go?     
                        if (guessupper<=guesslower) {
                            System.err.println(">> Ran out of space to guess");
                            cheatround=round+1;
                            System.out.println("Alice cheated in round "+cheatround);
                        }
                    }    
                }    
            }   
        }

        // Write an answer using System.out.println()
        // To debug: System.err.println("Debug messages...");


        if (cheatround==0) {
            System.out.println("No evidence of cheating");
        }
    }
}
