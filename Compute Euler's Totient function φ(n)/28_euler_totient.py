n = int(input("Enter a number: "))

result = n
temp = n
factor = 2

while factor * factor <= temp:
    if temp % factor == 0:
        while temp % factor == 0:
            temp //= factor
        result -= result // factor
    factor += 1

if temp > 1:
    result -= result // temp

print(f"Euler's Totient Function φ({n}) =", result)
