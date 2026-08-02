a = int(input("Enter the base: "))
b = int(input("Enter the exponent: "))

result = 1

while b > 0:
    if b % 2 == 1:
        result *= a

    a *= a
    b //= 2

print("Result =", result)
