MOD = 10 ** 9 + 7

for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()), reverse=True)

    s = 0

    for i in range(n):
        if a[i] - i < 1:
            break
        
        s += a[i] - i

    print(s % MOD)