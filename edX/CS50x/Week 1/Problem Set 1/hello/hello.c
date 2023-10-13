#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // taking input from the user
    string name = get_string("What's your name? ");

    // printing hello, name(the user inputted)
    printf("hello, %s\n", name);
}