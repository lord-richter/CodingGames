import java.util.*;
import java.io.*;
import java.math.*;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Solution {

    public static ArrayList<String> NumberDictionary = new ArrayList<String>(20);


    public static class MayanValue {
        // numerals are stored in DESCENDING order of power (20^2...20^1...etc)
        ArrayList<String> mayanNumerals = new ArrayList<String>();
        long decimal;
        int height;
        int width;

        // construct from stack of numerals ordered by decreasing power, 'height' lines per numeral
        public MayanValue(String[] stack,int width, int height) {
            this.height = height;
            this.width = width;
            this.decimal = 0;

            int numeralCount = stack.length / height;
            this.mayanNumerals = new ArrayList<String>(numeralCount);

            
            // top of stack (0,highest power) to bottom (N,lowest power)
            for (int i = 0; i<numeralCount ; i++) {
                // read each of the 'height' lines
                String numeral = "";
                for (int j=i*height;j<i*height+height;j++) {
                    numeral = numeral + stack[j];
                }   
                mayanNumerals.add(i, numeral);

                int base10 = NumberDictionary.indexOf(numeral);
                int power = numeralCount - i - 1;
                this.decimal = this.decimal + base10 * (int)Math.pow(20, power);

                System.err.printf("MayanValue (20^%d) [ %s ]  %d\n",power,numeral,base10);
                
            }

            System.err.printf("MayanValue is %d\n", decimal);

        }

        // constructor to covert a decimal value to mayan
        public MayanValue(long decimal, int width, int height) {
            this.height = height;
            this.width = width;
            this.decimal = decimal;

            if (decimal>0) {
                long remainder;
                long number = decimal;
                while (number>0) {
                    remainder = number%20;
                    number = number/20;
                    String numeral = NumberDictionary.get((int)remainder);
                    System.err.printf("Converting %d:  R:%d  N:%d   M:%s\n",decimal,remainder,number,numeral);
                    mayanNumerals.add(numeral);
                }
            } else {
                mayanNumerals.add(NumberDictionary.get(0));
            }

            // reverse order
            Collections.reverse(mayanNumerals);
        }


        public ArrayList<String> formatMayan() {
            ArrayList<String> output = new ArrayList<String>();

            // loop through all numerals
            for (String numeral : this.mayanNumerals) {
                // loop through each numeral and break it apart
                for (int i = 0;i<numeral.length();i+=width) {
                    output.add(numeral.substring(i, i+width));
                }
                System.err.printf("-->%s\n",numeral);
            }

            return output;
        }

        public long getDecimal() {
            return decimal;
        }

        public String toString() {
            ArrayList<String> formatter = formatMayan();
            String result = "";
            for (String line : formatter) {
                result = result + String.format("%s\n",line);
            }
            return result;
        }
    }

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int L = in.nextInt();
        int H = in.nextInt();
        // import the raw material for the number dictionary
        String[] rowTemp = new String[H];
        for (int i = 0; i < H; i++) {
            rowTemp[i] = in.next();
        }
        // create the number dictionary in a second loop, one number at a time
        for (int i = 0; i < 20; i++) {
            String number = "";
            // each number is made of H lines
            for (int j = 0; j < H; j++) {
                number = number + rowTemp[j].substring(i*L, (i*L)+L);
            }
            NumberDictionary.add(i, number);
        }

        NumberDictionary.forEach((n)->{System.err.printf("[ %s ]\n",n);});

        // read in the first value, where each number is H lines of L characters
        // organized in decreasing power, top to bottom
        int S1 = in.nextInt();
        String[] value1 = new String[S1];
        for (int i = 0; i < S1; i++) {
            value1[i]=(String)in.next();
        }

        MayanValue V1 = new MayanValue(value1,L,H);

        // read in the second value, where each number is H lines of L characters
        // organized in decreasing power, top to bottom
        int S2 = in.nextInt();
        String[] value2 = new String[S2];
        for (int i = 0; i < S2; i++) {
            value2[i]=(String)in.next();
        }

        MayanValue V2 = new MayanValue(value2,L,H);

        String operation = in.next();

        long DA = 0;

        System.err.printf("%d %s %d = ...\n",V1.getDecimal(),operation,V2.getDecimal());

        switch(operation) {
            case "+":
                DA = V1.getDecimal() + V2.getDecimal();
                break;
            case "-":
                DA = V1.getDecimal() - V2.getDecimal();
                break;
            case "*":
                DA = V1.getDecimal() * V2.getDecimal();
                break;
            case "/":
                DA = V1.getDecimal() / V2.getDecimal();
                break;
        }

        System.err.printf("ANSWER: %d\n",DA);
        MayanValue VA = new MayanValue(DA,L,H);
        System.out.println(VA.toString());

    }
}