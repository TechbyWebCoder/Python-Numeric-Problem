num = int(input("Enter a number: "))

original = num
sum_factorial = 0

while num > 0:
    digit = num % 10

    factorial = 1
    for i in range(1, digit + 1):
        factorial *= i

    sum_factorial += factorial
    num //= 10

if sum_factorial == original:
    print(original, "is a Strong Number")
else:
    print(original, "is Not a Strong Number")
