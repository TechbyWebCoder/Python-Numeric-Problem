start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

print("Deficient Numbers:")

for num in range(start, end + 1):

    divisor_sum = 0

    for i in range(1, num):
        if num % i == 0:
            divisor_sum += i

    if divisor_sum < num:
        print(num, end=" ")
