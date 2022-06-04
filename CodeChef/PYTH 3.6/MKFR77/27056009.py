n, x = map(int, input().split())
a = list(map(int, input().split()))

c = 0

for i in a:
    if i > x:
        c += 1

print(c)
