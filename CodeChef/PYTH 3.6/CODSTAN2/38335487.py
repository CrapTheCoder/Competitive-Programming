n = int(input())
a = [0] + list(map(int, input().split())) + [0]

m = int(input())

for _ in range(m):
    x, y = map(int, input().split())
    a[x-1] += y-1
    a[x+1] += a[x] - y
    a[x] = 0

for i in a[1:-1]:
    print(i)
