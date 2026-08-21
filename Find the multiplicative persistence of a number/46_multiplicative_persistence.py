num = int(input("Enter a number: "))

num = abs(num)
count = 0

while num >= 10:
    product = 1

    while num > 0:
        digit = num % 10
        product *= digit
        num //= 10

    num = product
    count += 1

print("Multiplicative Persistence =", count)
