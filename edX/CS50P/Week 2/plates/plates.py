def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if starts(s) == True and length(s) == True and (mid_ele(s) == True or alpha(s) == True or alpha_numeric(s) == True) and zero(s) == True:
        return True
    else:
        return False


def starts(s):
    if s[0:2].isalpha():
        return True
    else:
        return False


def length(s):
    if len(s) >= 2 and len(s) <= 6:
        return True
    else:
        return False


def mid_ele(s):
    for i in range(len(s)):
        if s[i].isdigit() and (s[i+1::].isnumeric()):
            return True
        else:
            return False


def zero(s):
    x = s.find("0")

    if x != -1 and s[x-1].isdigit():
        return True
    elif x == -1:
        return True
    else:
        return False


def alpha_numeric(s):
    if s.isalnum():
        return True
    else:
        return False


def alpha(s):
    if s.isalpha():
        return True
    else:
        return False


main()