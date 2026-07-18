start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

print("Palindromic Prime Numbers:")

for num in range(start, end + 1):

    if num < 2:
        continue

    # Check if the number is prime
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if not is_prime:
        continue

    # Reverse the number
    temp = num
    reverse = 0

    while temp > 0:
        digit = temp % 10
        reverse = reverse * 10 + digit
        temp //= 10

    # Check if palindrome
    if reverse == num:
        print(num, end=" ")
