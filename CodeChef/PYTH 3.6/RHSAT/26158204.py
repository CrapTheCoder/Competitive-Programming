c = 0

x = ''

m = -1

for j in range(int(input())):
    n = int(input().strip())
    m = max(m, n)

    if not j:
        x = ''.join(str(i) for i in range(1, n+1))
        c += int(x[n-1])
    else:
        if n < m:
            c += int(x[n-1])
        else:
            x += ''.join(str(i) for i in range(m, n+1))
            c += int(x[n-1])

print(c)
