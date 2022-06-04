n, k = map(int, input().split())
a = sorted(map(int, input().split()))

c = 0

for i in a:
    if k - i >= 0:
        k -= i
        c += 1
    else:
        break

print(c)