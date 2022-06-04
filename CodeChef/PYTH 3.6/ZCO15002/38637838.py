n, k = map(int, input().split())
a = sorted(map(int, input().split()))

j = 0
total = 0

for i in range(n):
    while j < n and a[j] - a[i] < k:
        j += 1

    total += n - j

print(total)
