num = int(input("Enter a number: "))

original = num
sum_digits = 0
product_digits = 1

while num > 0:
    digit = num % 10
    sum_digits += digit
    product_digits *= digit
    num //= 10

if sum_digits == product_digits:
    print(original, "is a Spy Number")
else:
    print(original, "is Not a Spy Number")
