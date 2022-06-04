n = int(input())
a = list(map(int, input().split()))
k = int(input())

for i in range(k, n+1):
    s = sorted(a[i-k:i])

    if k % 2:
        m = s[k // 2]
    else:
        m = (s[k // 2 - 1] + s[k // 2]) / 2

    print(m, end=' ')