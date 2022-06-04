n = int(input())
a = list(map(int, input().split()))

x = [0, 1] + [0 for _ in range(n - 1)]

for i in range(n):
    y = x[i] + 1

    for j in range(i - 1, -1, -1):
        if a[j:i+1] == a[j:i+1][::-1] and y > x[j] + 1:
            y = x[j] + 1

    x[i + 1] = y

print(x[n])
