def multiply(A, B):
    return [
        [
            A[0][0] * B[0][0] + A[0][1] * B[1][0],
            A[0][0] * B[0][1] + A[0][1] * B[1][1]
        ],
        [
            A[1][0] * B[0][0] + A[1][1] * B[1][0],
            A[1][0] * B[0][1] + A[1][1] * B[1][1]
        ]
    ]


def matrix_power(matrix, n):
    result = [[1, 0], [0, 1]]

    while n > 0:
        if n % 2 == 1:
            result = multiply(result, matrix)

        matrix = multiply(matrix, matrix)
        n //= 2

    return result


def fibonacci(n):
    if n == 0:
        return 0

    matrix = [[1, 1], [1, 0]]
    result = matrix_power(matrix, n)

    return result[0][1]


n = int(input("Enter the value of n: "))

if n < 0:
    print("Please enter a non-negative number.")
else:
    print(f"The {n}th Fibonacci Number =", fibonacci(n))
