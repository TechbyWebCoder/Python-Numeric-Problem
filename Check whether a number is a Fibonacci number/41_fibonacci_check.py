num = int(input("Enter a number: "))

a = 0
b = 1

while a < num:
    a, b = b, a + b

if a == num:
    print(num, "is a Fibonacci Number")
else:
    print(num, "is not a Fibonacci Number")
