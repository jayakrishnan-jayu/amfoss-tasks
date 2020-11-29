#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void) {
    long num;
    long copy;
    bool is_second = false;
    short int length;
    short int total;
    short int subTotal;
    bool isValid = true;
    do {
        num = get_long_long("Number: ");
        isValid = num>0;

        if(isValid) {

            copy = num;
            length = 0;
            total = 0;
            subTotal = 0;

            while(copy>0) {
                if(is_second) {

                    subTotal = copy%10 * 2;
                    while(subTotal>0) {
                        total += subTotal%10;
                        subTotal /= 10;
                    }
                    copy /= 10;
                    length++;
                    is_second = false;
                    continue;
                }

                total += copy%10;
                copy /= 10;
                length++;
                is_second = true;

            }

            if (total % 10 == 0) {
                if (length == 15) {
                        int begin = num/pow(10, length-2);
                        if (begin == 34 || begin == 37) {
                            printf("AMEX\n");
                            return 0;
                        }
                        printf("INVALID\n");
                        return 0;

                }
                else if (length == 16) {
                    int begin = num/pow(10, length-2);
                        if (begin >=51 && begin <=55) {
                            printf("MASTERCARD\n");
                            return 0;
                        }
                        printf("INVALID\n");
                        return 0;
                }
                else if (length == 13 || length == 16) {
                    int begin = num/pow(10,length-1);
                        if (begin == 4) {
                            printf("VISA\n");
                            return 0;
                        }
                        printf("INVALID\n");
                        return 0;
                }
                else {
                    printf("INVALID\n");
                    return 0;
                }
            }



        }


    } while(!isValid);

}