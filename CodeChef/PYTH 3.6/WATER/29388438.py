n = int(input())
a = list(map(int, input().split()))

m = -1

for i in range(n):
    c = 1

    j = i - 1

    while j >= 0 and a[j] <= a[j + 1]:
        j -= 1
        c += 1

    j = i + 1

    while j < n and a[j] <= a[j - 1]:
        j += 1
        c += 1

    m = max(m, c)

print(m)
