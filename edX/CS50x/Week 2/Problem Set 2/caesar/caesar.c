#include <cs50.h>
#include <ctype.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main(int argc, string argv[])
{
    if (argc == 2 && isdigit(*argv[1]))
    {
        int k = atoi(argv[1]);

        string p = get_string("plaintext: ");
        printf("ciphertext: ");

        int n = strlen(p);
        int c;
        for (int i = 0; i < n; i++)
        {
            if (isupper(p[i]))
            {
                int x = p[i] - 65;
                c = (x + k)%26;
                printf("%c", c + 65);
            }
            else if (islower(p[i]))
            {
                int y = p[i] - 97;
                c = (y + k)%26;
                printf("%c", c + 97);
            }
            else
            {
                printf("%c", p[i]);
            }
        }
        printf("\n");
        return 0;
    }
    else
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
}