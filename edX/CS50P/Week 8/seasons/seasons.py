from datetime import date
import operator
import sys
import inflect

p = inflect.engine()

def main():
    try:
        dob = input("Date of Birth: ")
        difference = operator.sub(date.today(), date.fromisoformat(dob))
        print(convert(difference.days))

    except ValueError:
        sys.exit("Invalid date")


def convert(day):
    time = day * 24 * 60
    return f"{(p.number_to_words(time, andword='')).capitalize()} minutes"


if __name__ == "__main__":
    main()