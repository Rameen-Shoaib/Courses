from cs50 import get_int

num = get_int("Height: ")
while True:
    if num < 1 or num > 8:
        num = get_int("Height: ")
    else:
        break

k = 1
x = 1
while x <= num:
    y = x
    while y <= num-1:
        print(end=" ")
        y += 1

    j = 1
    while j <= k:
        print("#", end="")
        j += 1

    print(end="  ")

    a = 1
    while a <= k:
        print("#", end="")
        a += 1

    k += 1
    x += 1

    print()