txt = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

check = txt.replace('-', ' ').lower().strip()

if check == "forty two" or check == "42":
     print("Yes")
else:
     print("No")
