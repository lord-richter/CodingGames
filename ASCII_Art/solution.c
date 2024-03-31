#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

int main()
{
    int charW;
    scanf("%d", &charW);
    int charH;
    scanf("%d", &charH); fgetc(stdin);
    char message[257];
    scanf("%[^\n]", message); fgetc(stdin);
    fprintf(stderr,">> %s\n",message);
    for (int i = 0; i < charH; i++) {
        char asciiRow[1025];
        scanf("%[^\n]", asciiRow); fgetc(stdin);

        int index = 0;
        char c = message[index];
        while (c!=0) {
            c = toupper(c);
            int letter = c - 65;  // ascii to letter of alphabet
            if (letter<0 || letter>25) { letter = 26;}
            // extract ascii portion for the letter
            // c does not care about buffer overruns in asciiRow
            // and neither do I
            char buffer[charW+1];
            memcpy(buffer,&asciiRow[(letter*charW)],charW);
            buffer[charW]=0;
            fprintf(stdout,"%s",buffer);
            index++;
            c = message[index];
        }
        printf("\n");
    }

    // Write an answer using printf(). DON'T FORGET THE TRAILING \n
    // To debug: fprintf(stderr, "Debug messages...\n");


    return 0;
}
