n = int(input())
a = list(map(int, input().split()))

mark = [1] * (n + 1)

for i in a:
    mark[i] = 0

print(*[i for i in range(1, n+1) if mark[i]])
