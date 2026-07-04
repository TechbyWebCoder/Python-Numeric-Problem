num = int(input("Enter a number: "))

square = num * num

if str(square).endswith(str(num)):
    print(num, "is an Automorphic Number")
else:
    print(num, "is Not an Automorphic Number")
