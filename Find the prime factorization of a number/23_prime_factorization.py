num = int(input("Enter a number: "))

print("Prime Factors:", end=" ")

while num % 2 == 0:
    print(2, end=" ")
    num //= 2

factor = 3

while factor * factor <= num:
    while num % factor == 0:
        print(factor, end=" ")
        num //= factor
    factor += 2

if num > 2:
    print(num, end=" ")
