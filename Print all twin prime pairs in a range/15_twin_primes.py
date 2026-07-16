start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

print("Twin Prime Pairs:")

for num in range(start, end - 1):

    # Check if num is prime
    is_prime1 = True
    if num < 2:
        is_prime1 = False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime1 = False
                break

    # Check if num + 2 is prime
    is_prime2 = True
    if num + 2 > end:
        is_prime2 = False
    else:
        for i in range(2, int((num + 2) ** 0.5) + 1):
            if (num + 2) % i == 0:
                is_prime2 = False
                break

    if is_prime1 and is_prime2:
        print(f"({num}, {num + 2})")
