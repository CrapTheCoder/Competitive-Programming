n = int(input())
a = list(map(int, input().split()))

t = 0
c = -1

for i in range(1, n):
    if a[i] < a[i-1]:
        if c == 1:
            c = -1
            t += 1

        elif c == -1:
            c = 0

    if a[i] > a[i-1]:
        if c == 0:
            c = -1
            t += 1

        elif c == -1:
            c = 1

print(t + 1)
