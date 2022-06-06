n, w = map(int, input().split())
a = list(map(int, input().split()))

p = [0]

for i in a:
p.append(p[-1] + i)

mini, maxi = min(p), max(p)

print(max(0, mini + w - maxi + 1))