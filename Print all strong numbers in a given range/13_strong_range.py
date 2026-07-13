start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

print("Strong Numbers:")

for num in range(start, end + 1):
    original = num
    total = 0
    temp = num

    while temp > 0:
        digit = temp % 10

        factorial = 1
        for i in range(1, digit + 1):
            factorial *= i

        total += factorial
        temp //= 10

    if total == original:
        print(original, end=" ")
