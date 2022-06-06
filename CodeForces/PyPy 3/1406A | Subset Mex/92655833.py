for _ in range(int(input())):
n = int(input())
a = sorted(map(int, input().split()))
c0 = c1 = 0

for i in a:
if c0 == i:
c0 += 1
continue

if c1 == i:
c1 += 1

print(c0 + c1)