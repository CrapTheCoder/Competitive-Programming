MOD = 10 ** 9 + 7

for _ in range(int(input())):
    n, a = map(int, input().split())

    ans = 0

    for i in range(1, n+1):
        ans += pow(a, 2*i-1, MOD)
        ans %= MOD

        a = pow(a, 2*i, MOD)

    print(ans)
