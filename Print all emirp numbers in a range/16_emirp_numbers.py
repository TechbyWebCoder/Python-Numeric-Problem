start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

print("Emirp Numbers:")

for num in range(start, end + 1):

    if num < 2:
        continue

    # Check if num is prime
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if not is_prime:
        continue

    # Reverse the number
    rev = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        rev = rev * 10 + digit
        temp //= 10

    # Skip palindromic primes
    if rev == num:
        continue

    # Check if reverse is prime
    is_rev_prime = True
    if rev < 2:
        is_rev_prime = False
    else:
        for i in range(2, int(rev ** 0.5) + 1):
            if rev % i == 0:
                is_rev_prime = False
                break

    if is_rev_prime:
        print(num, end=" ")
