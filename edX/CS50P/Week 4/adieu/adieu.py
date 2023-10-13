import inflect

p = inflect.engine()
mylist = []

while True:
    try:
         text = input("Name: ")
         mylist.append(text)

    except EOFError:
        print()
        print("Adieu, adieu, to", p.join(mylist))
        break