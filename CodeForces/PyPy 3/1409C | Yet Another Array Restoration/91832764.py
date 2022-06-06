from math import gcd

for _ in range(int(input())):
n, x, y = map(int, input().split())

mini = float('inf')
mina = []

for d in range(1, 50+1):
if (x - y) % d == 0:
ca = [x + d * i for i in range((y - x) // d + 1)]
ca.reverse()

for _ in range(n - len(ca)):
if ca[-1] - d <= 0:
break

ca.append(ca[-1] - d)

ca.reverse()

for _ in range(n - len(ca)):
ca.append(ca[-1] + d)

ca = sorted(ca)

if (len(ca) == n) and all(ca[i+1] - ca[i] == ca[n-1] - ca[n-2] for i in range(n-1)) and (x in ca) and (y in ca):
cm = max(ca)
if cm < mini:
mini = cm
mina = ca

print(*mina)