from math import sqrt

MAXN = 3005

spf = [0] * MAXN

def sieve():
spf[1] = 1
for i in range(2, MAXN):
spf[i] = i

for i in range(4, MAXN, 2):
spf[i] = 2

for i in range(3, int(sqrt(MAXN)) + 1):
if spf[i] == i:
for j in range(i * i, MAXN, i):
if spf[j] == j:
spf[j] = i


def factors(x):
while x != 1:
yield spf[x]
x //= spf[x]

sieve()

for _ in range(int(input())):
n = int(input())
a = list(map(int, input().split()))

b = [0] * n

cur = 1

for i in range(2, 105 + 1):
f = False

for j in range(n):
if not b[j]:
if not a[j] % i:
b[j] = cur
f = 1

if f:
cur += 1

print(max(b))
print(*b)