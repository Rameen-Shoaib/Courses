def main():
    s = input("Input: ")
    print(shorten(s))


def shorten(word):
    list = ["a", "e", "i", "o", "u"]
    new = ""

    for c in word:
        if c.lower() in list:
            continue
        new += c

    return new


if __name__ == "__main__":
    main()