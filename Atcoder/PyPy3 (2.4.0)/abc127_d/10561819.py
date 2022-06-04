n, m = map(int, input().split())
a = sorted(map(int, input().split()))

bc = []

for _ in range(m):
    bi, ci = map(int, input().split())

    bc.append((bi, ci))

bc.sort(reverse=True, key=lambda x: x[1])

i = 0

c = 0

for b, c in bc:
    j = 0

    while i < n and j < b and a[i] <= c:
        a[i] = c

        i += 1
        j += 1

print(sum(a))