def main():
    user = input("What time it is? ")
    ret = convert(user)

    if ret >= 7 and ret <= 8:
        print("breakfast time")
    elif ret >= 12 and ret <= 13:
        print("lunch time")
    elif ret >= 18 and ret <= 19:
        print("dinner time")
    else:
        exit()


def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)/60
    return (hours + minutes)

if __name__ == "__main__":
    main()