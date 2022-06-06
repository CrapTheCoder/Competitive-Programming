n = int(input())
a = list(map(int, input().split()))

m = max(a)

o = e = 0

for i in a:
if (m - i) % 2 == 0:
e += 1
else:
o += 1

print(min(e, o))