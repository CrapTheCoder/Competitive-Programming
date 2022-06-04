MOD = 10 ** 9 + 7

for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()), reverse=True)

    s = 0

    for i in range(n):
        s += max(0, a[i] - i)

    print(s % MOD)