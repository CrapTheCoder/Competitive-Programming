MOD = 1000000007

for _ in range(int(input())):
    n, k = map(int, input().split())

    assert 0 <= n <= 10 ** 9 and 1 <= k <= 10 ** 9

    if n == 0:
        print(k * (k - 1) % MOD)
        continue

    if k == 0:
        print(0)
        continue

    start = n ** 2
    skip = n * 2

    ans = start + skip * (k // 2)

    k = -(-k // 2)
    ans += k * (k - 1)

    print(ans % MOD)
