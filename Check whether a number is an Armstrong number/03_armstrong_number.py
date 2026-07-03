num = int(input("Enter a number: "))

original = num
digits = len(str(num))
sum_power = 0

while num > 0:
    digit = num % 10
    sum_power += digit ** digits
    num //= 10

if sum_power == original:
    print(original, "is an Armstrong Number")
else:
    print(original, "is Not an Armstrong Number")
