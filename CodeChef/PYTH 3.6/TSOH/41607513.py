def get(a):
    b = []
    s = 0
    m = float('-inf')

    for i in range(n):
        s += a[i]
        m = max(m, s)

        if s < 0:
            s = 0

        b.append(m)

    return b


n = int(input())
a = list(map(int, input().split()))

b = get(a)
c = get(a[::-1])[::-1]

maxi = -float('inf')
for i in range(n-1):
    maxi = max(maxi, b[i] + c[i+1])

print(maxi)
