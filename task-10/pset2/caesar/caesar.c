#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[]) {
    if (argc != 2) {
        printf("Usage: ./caesar k\n");
        return 1;
    }

    int k = atoi(argv[1]);
    string text = get_string("plaintext: ");
    char c;

    for (int i=0;  i<strlen(text); i++){

        if (isupper(text[i])) {
            c = ( ((int) text[i]+k)-65 ) % 26 + 65;
        }
        else if  (islower(text[i])) {
            c = ( ((int) text[i]+k)-97 ) % 26 + 97;
        }
        else c = text[i];
        printf("%c",c);
    }

    return 0;
}