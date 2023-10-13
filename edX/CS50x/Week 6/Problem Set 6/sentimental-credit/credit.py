from cs50 import get_string
import re

# taking input
num = get_string("Number: ")

while num.isdigit() == False:
    num = get_string("Number: ")

length = len(num)

# checking pattern
amex = '^[3][4|7][0-9]+$'
result1 = bool(re.match(amex, num))

mastercard = '^[5][1|2|3|4|5][0-9]+$'
result2 = bool(re.match(mastercard, num))

visa = '^[4][0-9]+$'
result3 = bool(re.match(visa, num))

# how many times loop runs
if length == 13:
    n = 7
elif length == 15 or length == 16:
    n = 8
else:
    n = int(round(length/2))

x = length - 2
y = length - 1
sum = 0
total = 0
# checking if the number is valid
for i in range(n):
    val = 2 * int(num[x])

    if val > 9:
        val = val - 9

    sum += val

    value = int(num[y])
    total += value

    x -= 2
    y -= 2

if (length == 15):
    if sum > 40:
        final = sum + total - 2
    else:
        final = sum + total - 1
elif (length == 13):
    final = sum + total - 4
else:
    final = sum + total

# after checking validity, we check which type of number it is
if final % 10 == 0:
    if (length == 15 and result1 == True):
        print("AMEX")
    elif ((length == 13 or length == 16) and result3 == True):
        print("VISA")
    elif (length == 16 and result2 == True):
        print("MASTERCARD")
    else:
        print("INVALID")
else:
        print("INVALID")