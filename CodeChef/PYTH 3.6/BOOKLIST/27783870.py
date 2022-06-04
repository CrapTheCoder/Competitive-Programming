n = int(input())
a = list(map(int, input().split()))
m = int(input())

x = []

for _ in range(m):
    i = int(input())
    i -= 1

    print(a[i])
    del a[i]
