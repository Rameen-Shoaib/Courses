months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

date = input("Date: ").strip()

while True:
    try:
        if ("/") in date:
            if date.isalnum():
                    date = input("Date: ")

            m, d, y = date.split("/")

            # reprompt if spaces
            for x in date:
                 if " " in x:
                     date = input("Date: ")

            mon = m.zfill(2)
            day = d.zfill(2)

            if int(d)> 31 or int(m) > 12:
                date = input("Date: ")

            print(f"{y}-{mon}-{day}")
            break

        elif (",") in date:
            dat, y = date.split(", ")
            m, d = dat.split(" ")

            if int(d) > 31:
                date = input("Date: ")

            mnth = str(months.index(m) + 1)

            mon = mnth.zfill(2)
            day = d.zfill(2)

            print(f"{y}-{mon}-{day}")
            break

    except ValueError:
        date = input("Date: ")

    else:
        continue