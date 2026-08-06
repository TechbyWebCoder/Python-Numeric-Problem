n = int(input("Enter n: "))
r = int(input("Enter r: "))

if r > n or r < 0:
    print("Invalid Input")
else:
    factorial_n = 1
    factorial_nr = 1

    for i in range(1, n + 1):
        factorial_n *= i

    for i in range(1, (n - r) + 1):
        factorial_nr *= i

    nPr = factorial_n // factorial_nr

    print(f"{n}P{r} =", nPr)
