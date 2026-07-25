num = int(input("Enter a number: "))

count = 0

for i in range(1, int(num ** 0.5) + 1):
    if num % i == 0:
        count += 1

        if i != num // i:
            count += 1

print("Total Number of Divisors =", count)
