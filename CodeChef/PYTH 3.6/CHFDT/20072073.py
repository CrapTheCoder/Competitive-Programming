n, l = map(int, input().split())
s = input()

a = []
b = []

for _ in range(n):
    x = input()
    t = ((sum(i != j for i, j in zip(s, x))) / len(s)) * 100

    a.append(t)
    b.append(x)

print(b[a.index(min(a))])