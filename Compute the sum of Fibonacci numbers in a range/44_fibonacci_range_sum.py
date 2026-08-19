def fibonacci(n):
    a = 0
    b = 1

    for _ in range(n):
        a, b = b, a + b

    return a


start = int(input("Enter starting term: "))
end = int(input("Enter ending term: "))

if start < 0 or end < 0 or start > end:
    print("Invalid Range")
else:
    total = fibonacci(end + 2) - fibonacci(start + 1)

    print(f"Sum of Fibonacci numbers from F({start}) to F({end}) =", total)
