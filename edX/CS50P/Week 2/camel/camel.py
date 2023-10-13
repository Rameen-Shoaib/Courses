text = input("camelCase: ")
print("snake_case: ", end="")

for character in text:
    if character.isupper():
        print('_', end="")
        print(character.lower(), end="")
    else:
        print(character, end="")
print()
