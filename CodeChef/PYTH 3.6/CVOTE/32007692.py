n, m = map(int, input().split())

d = {}

cv = {}
nv = {}

for _ in range(n):
    name, country = input().split()
    d[name] = country

    cv[country] = 0
    nv[name] = 0

for _ in range(m):
    name = input()

    cv[d[name]] += 1
    nv[name] += 1

ckv = [(votes, name) for name, votes in cv.items()]
nkv = [(votes, name) for name, votes in nv.items()]

ckv.sort(key=lambda x: x[1])
ckv.sort(key=lambda x: -x[0])

nkv.sort(key=lambda x: x[1])
nkv.sort(key=lambda x: -x[0])

print(ckv[0][1])
print(nkv[0][1])