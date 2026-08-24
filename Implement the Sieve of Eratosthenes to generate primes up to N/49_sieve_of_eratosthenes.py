n = int(input("Enter the value of N: "))

if n < 2:
    print("There are no prime numbers up to", n)
else:
    is_prime = [True] * (n + 1)

    is_prime[0] = False
    is_prime[1] = False

    p = 2

    while p * p <= n:
        if is_prime[p]:
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False

        p += 1

    print("Prime numbers up to", n, "are:")

    for i in range(2, n + 1):
        if is_prime[i]:
            print(i, end=" ")
