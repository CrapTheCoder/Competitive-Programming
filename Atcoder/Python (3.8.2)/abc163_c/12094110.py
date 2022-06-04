n = int(input())
a = list(map(int, input().split()))

g = [[] for _ in range(n)]

for i in range(n-1):
    g[a[i]-1].append(i)

for i in g:
    print(len(i))