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

    string keyword = argv[1];
    for (int i=0; i<strlen(keyword); i++){
        if (!isalpha(keyword[i])) {
            printf("Usage: ./caesar k\n");
            return 1;
        }
    }

    string text = get_string("plaintext: ");
    char c;
    int l;
    int k;
    int counter = 0;
    for (int i=0;  i<strlen(text); i++){

        k = (int) keyword[counter];
        if (isupper(keyword[counter]))
            k-=65;
        else
            k-=97;

        if (isupper(text[i])) {
            counter += 1;
            c = ( ((int) text[i]+k)-65 ) % 26 + 65;
        }
        else if  (islower(text[i])) {
            counter += 1;
            c = ( ((int) text[i]+k)-97 ) % 26 + 97;
        }
        else c = text[i];
        printf("%c",c);
        if (counter == strlen(keyword))
            counter = 0;
    }

    return 0;
}