MOD = 10 ** 9 + 7

for _ in range(int(input())):
    i, j = map(int, input().split())

    print(pow(j + 2, i * (i + 1) // 2, MOD))
