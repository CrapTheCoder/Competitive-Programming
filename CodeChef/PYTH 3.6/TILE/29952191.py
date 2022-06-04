from copy import deepcopy


class MatrixExpo:
    def __init__(self, orig, mod=0):
        self.orig = [orig[::-1]]
        self.length = len(self.orig[0])

        self.mod = mod

    @staticmethod
    def identity(n):
        matrix = [[0] * n for _ in range(n)]

        for i in range(n):
            matrix[i][i] = 1

        return matrix

    def multiply(self, mat1, mat2, copy):
        r1, r2 = len(mat1), len(mat2)
        c1, c2 = len(mat1[0]), len(mat2[0])

        result = [[0] * c2 for _ in range(r1)]

        for i in range(r1):
            for j in range(c2):
                for k in range(r2):
                    result[i][j] += mat1[i][k] * mat2[k][j]

                    if self.mod != 0:
                        result[i][j] %= self.mod

        for i in range(r1):
            for j in range(c2):
                copy[i][j] = result[i][j]

    def power(self, mat, n):
        res = self.identity(len(mat))

        while n:
            if n & 1:
                self.multiply(res, mat, res)

            self.multiply(mat, mat, mat)

            n >>= 1

        return res

    def zibo(self, n):
        orig = deepcopy(self.orig)
        length = self.length

        if n < length:
            return orig[0][length - n - 1]

        magic = []

        for i in range(length):
            a = [0] * length
            a[0] = 1

            if i + 1 < length:
                a[i + 1] = 1

            magic.append(a)

        magic = self.power(magic, n - length + 1)

        self.multiply(orig, magic, orig)

        return orig[0][0]

expo = MatrixExpo([0, 1], 10 ** 9 + 7)

for _ in range(int(input())):
    n = int(input())

    print(expo.zibo(n + 1))