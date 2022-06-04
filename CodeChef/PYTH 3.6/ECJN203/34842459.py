n = int(input())
d = []

for i in range(n):
    x, y = map(int, input().split())

    d.append((x, y, i+1))

d.sort(key=lambda x: -x[2])
d.sort(key=lambda x: -x[0])
d.sort(key=lambda x: x[1])

print(*[i[-1] for i in d])