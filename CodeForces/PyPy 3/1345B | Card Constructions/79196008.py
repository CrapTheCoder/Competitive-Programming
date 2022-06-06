from bisect import bisect

l = [2]

i = 1

while l[-1] <= 10 ** 9:
i += 1
l.append(l[-1] + 2 * i)

for i in range(len(l)):
l[i] += i * (i+1) // 2

for _ in range(int(input())):
n = int(input())

c = 0

while True:
x = bisect(l, n)

if x != 0 and l[x] > n:
x -= 1

n -= l[x]

if n < 0:
break

c += 1

print(c)