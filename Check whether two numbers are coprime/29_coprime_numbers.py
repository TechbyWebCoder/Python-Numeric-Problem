a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

x = a
y = b

# Find GCD using Euclidean Algorithm
while y != 0:
    x, y = y, x % y

if x == 1:
    print(a, "and", b, "are Coprime Numbers")
else:
    print(a, "and", b, "are Not Coprime Numbers")
