num = int(input("Enter a number: "))

square = num * num
sum_digits = 0
temp = square

while temp > 0:
    digit = temp % 10
    sum_digits += digit
    temp //= 10

if sum_digits == num:
    print(num, "is a Neon Number")
else:
    print(num, "is Not a Neon Number")
