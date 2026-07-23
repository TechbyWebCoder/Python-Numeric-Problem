num = int(input("Enter a number: "))

largest_prime = -1

while num % 2 == 0:
    largest_prime = 2
    num //= 2

factor = 3

while factor * factor <= num:
    while num % factor == 0:
        largest_prime = factor
        num //= factor
    factor += 2

if num > 2:
    largest_prime = num

print("Largest Prime Factor =", largest_prime)
