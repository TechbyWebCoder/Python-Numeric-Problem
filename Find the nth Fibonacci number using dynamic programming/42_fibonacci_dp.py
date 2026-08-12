n = int(input("Enter the value of n: "))

if n < 0:
    print("Please enter a non-negative number.")
elif n == 0:
    print("Fibonacci Number = 0")
elif n == 1:
    print("Fibonacci Number = 1")
else:
    dp = [0] * (n + 1)

    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    print(f"The {n}th Fibonacci Number =", dp[n])
