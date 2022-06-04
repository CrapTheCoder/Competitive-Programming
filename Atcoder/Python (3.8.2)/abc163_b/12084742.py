n, m = map(int, input().split())
a = list(map(int, input().split()))

s = sum(a)

n -= s

if n < 0:
    print(-1)
else:
    print(n)