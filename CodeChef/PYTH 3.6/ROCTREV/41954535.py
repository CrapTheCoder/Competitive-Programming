MOD = 10 ** 9 + 7

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    i, j = map(int, input().split())

    f = 1
    for k in range(i, j):
        f *= a[k]
        f %= MOD

    print(f)
