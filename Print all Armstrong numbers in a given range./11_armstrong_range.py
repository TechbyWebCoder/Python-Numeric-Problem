start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

print("Armstrong Numbers:")

for num in range(start, end + 1):
    original = num
    digits = len(str(num))
    total = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    if total == original:
        print(original, end=" ")
