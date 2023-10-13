#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int i;
    do
    {
        i = get_int("Start size: ");
    }
    while (i < 9);

    // TODO: Prompt for end size
    int j;
    do
    {
        j = get_int("End size: ");
    }
    while (j < i);

    // TODO: Calculate number of years until we reach threshold
    int z = 0;
    int n = 0;
    while (z < j)
    {
        int x = i/3;
        int y = i/4;
        z = i + x - y;
        i = z;
        n += 1;
        if (z >= j)
        {
            // TODO: Print number of years
            printf("Years: %i\n", n);
        }
    }
}
