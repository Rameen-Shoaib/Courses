grocery = []
tally = {}

while True:
    try:
        item = input().upper().strip()

        grocery.append(item)
        grocery.sort()

    except EOFError:
        print()

        for item in grocery:
            if item in tally:
                tally[item] += 1
            else:
                tally[item] = 1

        for x in tally:
            print(str(tally[x]) + " " + x)

        break

    except KeyError:
        pass

    else:
        continue

