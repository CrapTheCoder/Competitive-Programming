n, k = map(int, input().split())
a = sorted(map(int, input().split()))

x = 0
i = j = 0

while i < n:
    if j < i:
        j = i
    elif j >= n:
        break

    if a[j] - a[i] >= k:
        i += 1
        x += n - j
    else:
        j += 1

print(x)