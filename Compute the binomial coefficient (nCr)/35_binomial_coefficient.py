n = int(input("Enter n: "))
r = int(input("Enter r: "))

if r > n or r < 0:
    print("Invalid Input")
else:
    factorial_n = 1
    factorial_r = 1
    factorial_nr = 1

    for i in range(1, n + 1):
        factorial_n *= i

    for i in range(1, r + 1):
        factorial_r *= i

    for i in range(1, (n - r) + 1):
        factorial_nr *= i

    nCr = factorial_n // (factorial_r * factorial_nr)

    print(f"{n}C{r} =", nCr)
