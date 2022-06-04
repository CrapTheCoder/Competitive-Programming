n, t = map(int, input().split())
a = list(map(int, input().split()))

s = sum(a)
x = t // s * n
t -= t // s * s

i = 0
while a:
    ind = []
    for j, i in enumerate(a):
        if t < i:
            ind.append(j)

    for i in ind[::-1]:
        a.pop(i)

    for j in a:
        if t >= j:
            t -= j
            x += 1

print(x)
