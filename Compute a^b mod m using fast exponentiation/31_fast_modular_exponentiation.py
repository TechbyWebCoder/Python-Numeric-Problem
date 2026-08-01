a = int(input("Enter base (a): "))
b = int(input("Enter exponent (b): "))
m = int(input("Enter modulus (m): "))

result = 1
a = a % m

while b > 0:
    if b % 2 == 1:
        result = (result * a) % m

    a = (a * a) % m
    b //= 2

print("Result =", result)
