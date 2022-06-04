from typing import List
Matrix = List[List[int]]

MOD = 10 ** 9 + 7


def identity(n: int) -> Matrix:
    matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        matrix[i][i] = 1

    return matrix


def multiply(mat1: Matrix, mat2: Matrix, copy: Matrix) -> None:
    r1, r2 = len(mat1), len(mat2)
    c1, c2 = len(mat1[0]), len(mat2[0])

    result = [[0] * c2 for _ in range(r1)]

    for i in range(r1):
        for j in range(c2):
            for k in range(r2):
                result[i][j] = (result[i][j] + mat1[i][k] * mat2[k][j]) % MOD

    for i in range(r1):
        for j in range(c2):
            copy[i][j] = result[i][j]


def power(mat: Matrix, n: int) -> Matrix:
    res = identity(len(mat))

    while n:
        if n & 1:
            multiply(res, mat, res)

        multiply(mat, mat, mat)

        n >>= 1

    return res


def fib(n: int) -> int:
    if n == 0:
        return 0

    magic = [[2, 1],
             [2, 0]]

    mat = power(magic, n)

    return mat[0][0]

for _ in range(int(input())):
    n = int(input())

    print(fib(n) % MOD)
