n, d = map(int,input().split())
a = sorted(int(input()) for _ in range(n))

i = 1
k = a[0]
count = 0

while i < n:
    if a[i] - k <= d:
        count += 1
        i += 1

    if i >= n:
        break

    k = a[i]
    i += 1

print(count)