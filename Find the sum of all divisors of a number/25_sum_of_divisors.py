num = int(input("Enter a number: "))

divisor_sum = 0

for i in range(1, int(num ** 0.5) + 1):
    if num % i == 0:
        divisor_sum += i

        if i != num // i:
            divisor_sum += num // i

print("Sum of All Divisors =", divisor_sum)
