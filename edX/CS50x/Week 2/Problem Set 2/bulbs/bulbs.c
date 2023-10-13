#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int arrays[]);

int main(void)
{
    // TODO
    string input = get_string("Message: ");

    int n = strlen(input);
    int array[n];
    int arr[BITS_IN_BYTE];
    int x, y, j;

    for (int i = 0; i < n; i++)
    {
        array[i] = input[i];
        y = array[i];

        while (y != 0)
        {
            x = round(y % 2);
            y = y / 2;

            for (j = 0; j < BITS_IN_BYTE; j++)
            {
                if (x == 0)
                {
                    arr[j] = x;
                    break;
                }
                else
                {
                    arr[j] = x;
                    break;
                }
            }
            print_bulb(arr);
        }
        printf("\n");
    }
}


void print_bulb(int arrays[])
{
    for (int a = 0; a < 1; a++)
    {
        if (arrays[a] == 0)
        {
            // Dark emoji
            printf("\U000026AB");
        }
        else if (arrays[a] == 1)
        {
            // Light emoji
            printf("\U0001F7E1");
        }
    }
}
