cal = input("Expression: ")

x,y,z = cal.split(' ')
x = int(x)
z = int(z)

if y == '+':
    cal = x + z
elif y == '-':
    cal = x - z
elif y == '*':
    cal = x * z
elif y == '/':
    cal = x / z

print(f"{cal:.1f}")