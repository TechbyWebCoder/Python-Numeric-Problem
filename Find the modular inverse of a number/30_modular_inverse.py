a = int(input("Enter the number (a): "))
m = int(input("Enter the modulus (m): "))

original_m = m
x0, x1 = 0, 1

if m == 1:
    print("Modular Inverse does not exist")
else:
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0

    if a != 1:
        print("Modular Inverse does not exist")
    else:
        if x1 < 0:
            x1 += original_m
        print("Modular Inverse =", x1)
