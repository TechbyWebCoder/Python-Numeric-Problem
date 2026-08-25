import math

def segmented_sieve(L, R):
    # Handle values less than 2
    if R < 2:
        return []

    L = max(L, 2)

    # Find primes up to sqrt(R)
    limit = math.isqrt(R)

    is_prime = [True] * (limit + 1)
    is_prime[0] = False
    is_prime[1] = False

    primes = []

    for i in range(2, limit + 1):
        if is_prime[i]:
            primes.append(i)

            for j in range(i * i, limit + 1, i):
                is_prime[j] = False

    # Create a segment for [L, R]
    segment = [True] * (R - L + 1)

    # Mark multiples of each prime
    for p in primes:
        start = max(p * p, ((L + p - 1) // p) * p)

        for j in range(start, R + 1, p):
            segment[j - L] = False

    # Collect primes
    result = []

    for i in range(L, R + 1):
        if segment[i - L]:
            result.append(i)

    return result


L = int(input("Enter the lower limit: "))
R = int(input("Enter the upper limit: "))

if L > R:
    print("Invalid Range")
else:
    primes = segmented_sieve(L, R)

    print("Prime numbers in the range:")
    print(*primes)
