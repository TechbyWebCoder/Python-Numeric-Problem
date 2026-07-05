num = int(input("Enter a number: "))

original = num
sum_digits = 0

while num > 0:
    digit = num % 10
    sum_digits += digit
    num //= 10

if original % sum_digits == 0:
    print(original, "is a Harshad (Niven) Number")
else:
    print(original, "is Not a Harshad (Niven) Number")
