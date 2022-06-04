n, k = map(int, input().split())
a = sorted(map(int, input().split()))

c = 0

j = 0

for i in range(n):
    while a[j] - a[i] < k:
        j += 1

        if j == n:
            break
    else:
        c += n - j
        continue

    if j == n:
        break

print(c)
