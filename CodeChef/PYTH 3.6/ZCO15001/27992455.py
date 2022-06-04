n = int(input())
a = input().split()

c = [float('inf')] * (n + 1)
c[0] = 0

for i in range(1, n + 1):
    for j in range(i + 1):
        if a[j:i] == a[j:i][::-1]:
            c[i] = min(c[j] + 1, c[i])

print(c[-1])
