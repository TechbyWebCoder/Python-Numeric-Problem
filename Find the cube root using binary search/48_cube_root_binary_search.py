n = float(input("Enter a number: "))

if n == 0:
    print("Cube Root = 0")
else:
    negative = n < 0
    n = abs(n)

    low = 0
    high = max(1, n)

    # Binary search for cube root
    for _ in range(100):
        mid = (low + high) / 2

        if mid ** 3 < n:
            low = mid
        else:
            high = mid

    cube_root = (low + high) / 2

    if negative:
        cube_root = -cube_root

    print("Cube Root =", cube_root)
