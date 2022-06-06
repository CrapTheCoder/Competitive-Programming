n = int(input())
a = sorted(map(int, input().split()))
c = 1

i = 0
while True:
while i < n and a[i] < c:
i += 1

if i == n:
break

i += 1
c += 1

print(c-1)