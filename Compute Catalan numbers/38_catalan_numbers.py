n = int(input("Enter the value of n: "))

catalan = 1

for i in range(n):
    catalan = catalan * (2 * i + 2) // (i + 2)

print(f"Catalan Number C({n}) =", catalan)
