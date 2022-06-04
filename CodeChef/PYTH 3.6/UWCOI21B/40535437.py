n, m = map(int, input().split())
a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()))
c = 0

for i in b:
    if a[0] > i:
        c += n

print(c)
