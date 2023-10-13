#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n;
    n = get_int("Height: ");
    while (n < 1 || n > 8)
    {
        n = get_int("Height: ");
    }

    int k = 1;
    for (int x = 1; x <= n; x++)
    {
        for (int y = x; y <= n-1; y++)
        {
            printf(" ");
        }

        for (int j = 1; j <= k; j++)
        {
            printf("#");
        }
        k += 1;

        printf("\n");
    }
}