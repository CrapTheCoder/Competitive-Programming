MOD = 10 ** 9 + 7

for _ in range(int(input())):
    n = int(input())

    print((2 ** n - 1) % MOD, (2 ** n) % MOD)
