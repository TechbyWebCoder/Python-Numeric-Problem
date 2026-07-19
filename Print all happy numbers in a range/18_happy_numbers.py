start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

print("Happy Numbers:")

for num in range(start, end + 1):
    original = num
    visited = set()

    while num != 1 and num not in visited:
        visited.add(num)
        total = 0

        while num > 0:
            digit = num % 10
            total += digit * digit
            num //= 10

        num = total

    if num == 1:
        print(original, end=" ")
