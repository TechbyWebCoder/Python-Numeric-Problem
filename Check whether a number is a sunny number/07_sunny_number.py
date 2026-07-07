num = int(input("Enter a number: "))

next_num = num + 1
root = int(next_num ** 0.5)

if root * root == next_num:
    print(num, "is a Sunny Number")
else:
    print(num, "is Not a Sunny Number")
