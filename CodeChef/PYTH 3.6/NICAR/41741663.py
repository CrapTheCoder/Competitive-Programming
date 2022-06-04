n = int(input())
a = list(map(int, input().split()))
p = [a[0]]
mx = a[0]

for i in range(1, n):
    p.append(a[i] + mx)
    mx = max(mx, p[-1])

print(*p)
