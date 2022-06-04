MOD = 10 ** 9 + 7
for _ in range(int(input())):
    n, m = map(int, input().split())
    x = n // 2

    print(pow(m, (x * (x + 1)), MOD))
