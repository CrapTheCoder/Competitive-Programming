for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    d = {}
    for i in range(n):
        for j in range(32):
            if (a[i] >> j) & 1:
                d[j] = d.get(j, 0) + 1

    ans = 0
    for i in d:
        if d[i] > 1:
            ans |= 1 << i

    print(ans)