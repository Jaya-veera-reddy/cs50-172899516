
expression = input("Expression: ").strip()

x, y, z = expression.split()

x = int(x)
z = int(z)

if y == '+':
    result = x + z
elif y == '-':
    result = x - z
elif y == '*':
    result = x * z
elif y == '/':
    result = x / z
else:
    print("Invalid y")
    exit()

print(f"{result:.1f}")
