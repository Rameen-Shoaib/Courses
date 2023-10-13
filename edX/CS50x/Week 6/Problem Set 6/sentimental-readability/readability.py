from cs50 import get_string

def main():
    text = get_string("Text: ")

    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    L = letters / words * 100
    S = sentences / words * 100

    grade = round(0.0588 * L - 0.296 * S - 15.8)

    if (grade < 1):
        print("Before Grade 1")

    elif (grade >= 16):
        print("Grade 16+")

    else:
        print(f"Grade {grade}")


def count_letters(text):
    count1 = 0
    n = len(text)
    for i in range(n):
        if text[i].isalpha():
            count1 += 1
    return count1

def count_words(text):
    count2 = 1
    n = len(text)
    for i in range(n):
        if text[i].isspace():
            count2 += 1
    return count2

def count_sentences(text):
    count3 = 0
    n = len(text)
    for i in range(n):
        if text[i] == '.' or text[i] == '!' or text[i] == '?':
            count3 += 1
    return count3

main()