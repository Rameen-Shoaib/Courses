import random

def main():
    lvl = get_level()
    score = 0
    mistake = 0

    for i in range(10):
        x, y = generate_integer(lvl)

        answer = int(input(f"{x} + {y} = "))

        if answer == (x+y):
            score += 1

        while answer != (x+y):
            print("EEE")
            mistake += 1
            answer = int(input(f"{x} + {y} = "))

            if mistake == 2:
                    print("EEE")
                    add = x+y
                    print(x, "+", y, "=", add)
                    break

    print("Score: " + str(score))


def get_level():
    while True:
        try:
            x = int(input("Level: "))

            if x == 1 or x == 2 or x == 3:
                return x
            else:
                x = int(input("Level: "))

        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)

    return x, y


if __name__ == "__main__":
    main()