n = int(input("Enter a number: "))

if n < 0:
    print("Integer square root is not defined for negative numbers")
else:
    low = 0
    high = n
    answer = 0

    while low <= high:
        mid = (low + high) // 2

        if mid * mid <= n:
            answer = mid
            low = mid + 1
        else:
            high = mid - 1

    print("Integer Square Root =", answer)
