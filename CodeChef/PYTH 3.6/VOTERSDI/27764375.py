n1, n2, n3 = map(int, input().split())

c = {}

for i in range(n1):
    x = int(input())
    c[x] = c.get(x, 0) + 1

for i in range(n2):
    x = int(input())
    c[x] = c.get(x, 0) + 1

for i in range(n3):
    x = int(input())
    c[x] = c.get(x, 0) + 1

d = [i for i, j in zip(c.keys(), c.values()) if j >= 2]

print(len(d))
print(*sorted(d), sep='\n')
