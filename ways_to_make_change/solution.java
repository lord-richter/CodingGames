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
        int sum = in.nextInt();

        int S = in.nextInt();
        Integer[] coin = new Integer[S];

        for (int i = 0; i < S; i++) {
            coin[i] = in.nextInt();
        }

        System.err.printf("SUM: %d\n",sum);
        
        int[][] paths = new int[S+1][sum+1];

        // starting point
        // if the number of coins is 0 and the sum is 0
        // then there is only one way to get 0, and that is using 0
        paths[0][0]=1;

        // go through all of the coins
        // For each possible value between 0 and SUM, calculate 
        // the number of different coins that can be used to make that total
        for (int c=1;c<=coin.length;c++) {
            int v = coin[c-1];

            // within each coin, work through the possible results (r=sum-coin for all coin 0 to sum)
            for (int r=0;r<=sum;r++) {
                // the path to get to this result with this coin
                // is the number of times we got the same result from
                // the previous coin and we will add to that if this coin can 
                // also be used. This accounts for getting here using the 
                // the previous coin
                paths[c][r] = paths[c-1][r];

                // if the value of this coin is less than or equal to
                // the current result, then we can use this coin to get there.
                if (coin[c-1]<=r) {
                    // to this coin and result, we add in the 
                    // number of times we got the same difference 
                    // with this coin. This accounts for getting here using
                    // this coin more than once
                    paths[c][r] += paths[c][r - coin[c-1]];
                }
            }
        }

        // dump out the array
        for (int i = 0;i<=S; i++) {
            System.err.printf("%d: ",i>0?coin[i-1]:0);
            for (int j = 0;j<=sum;j++) {
                System.err.printf(" %d",paths[i][j]);
            }
            System.err.println();
        }


        // the answer has been carried forward during the
        // calculation loops and will be the upper right
        // corner of the array
        System.out.println(paths[S][sum]);
    }
}
