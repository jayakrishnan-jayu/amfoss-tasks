#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n;
    bool isInvalid;
    do
    {
      n = get_int("Enter a number : ");
      isInvalid = n<0 || n>23;
      if (!isInvalid)
      for (int i=0; i<n; i++)
      {
          for (int j=0; j<n-i-1; j++) printf(" ");
          for (int j=0; j<i+1; j++) printf("#");
          printf("  ");
          for (int j=0; j<i+1; j++) printf("#");
          printf("\n");
      }
    } while (isInvalid);
  return 0;
}