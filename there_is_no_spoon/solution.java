import java.util.*;
import java.io.*;
import java.math.*;

/**
 * Don't let the machines win. You are humanity's last hope...
 **/
class Player {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int width = in.nextInt(); // the number of cells on the X axis
        int height = in.nextInt(); // the number of cells on the Y axis
        if (in.hasNextLine()) {
            in.nextLine();
        }
        String[] row = new String[height];

        for (int i = 0; i < height; i++) {
            row[i] = in.nextLine(); // width characters, each either 0 or .
        }

        int x1,y1,x2,y2,x3,y3;

        // each row in sequence
        for (y1=0;y1<height;y1++) {
            // each position in the row
            for (x1=0;x1<width;x1++) {
                // is this a node?
                if (row[y1].charAt(x1)=='0') {
                    // set initial guesses for x2 y2 x3 y3
                    x2=x1+1; // next column
                    x3=x1; // same column for any row
                    y2=y1; // same row
                    y3=y1+1; // at least the next row

                    // find node to the right, if there is one
                    // this will loop from x2=x1+1 to x2=width, the latter being invalid
                    for (;x2<width && row[y1].charAt(x2)!='0';x2++) {}
                    // if there is none, -1 -1
                    if (x2>=width) {
                        x2=-1;
                        y2=-1;
                    }
                    
                    // find node to the bottom, if there is one
                    // this will loop from y3=y1+1 to y3=height, the latter being invalid
                    for (;y3<height && row[y3].charAt(x3)!='0';y3++) {}
                    // if there is none, -1 -1
                    if (y3>=height) {
                        x3=-1;
                        y3=-1;
                    }

                    // display the 6 numbers
                    System.out.printf("%d %d %d %d %d %d\n", x1,y1,x2,y2,x3,y3);

                } // this is not the node we are looking for
            }
        }

    }
}