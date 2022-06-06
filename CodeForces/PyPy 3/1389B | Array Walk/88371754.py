for _ in range(int(input())):
n, k, z = map(int, input().split())
a = list(map(int, input().split()))

p = [a[0]]

for i in range(1, n):
p.append(p[-1] + a[i])

s = p[k]

for i in range(1, k+1):
k -= 1
r = k

cs = 0
cz = z

m = 0

while r > 0:
if m % 2 == 0:
if cz > 0:
cs += a[i-1]
cz -= 1
else:
break

else:
cs += a[i]

r -= 1
s = max(s, cs + p[i + r - 1])

m += 1

s = max(s, cs + p[i + r])

print(s)