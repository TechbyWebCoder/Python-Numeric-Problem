n = int(input("Enter a number: "))

count = 0

while n > 0:
    n //= 5
    count += n

print("Trailing Zeros =", count)
