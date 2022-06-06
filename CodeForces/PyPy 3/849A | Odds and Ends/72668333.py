n = int(input())
a = list(map(int, input().split()))

flag = False

i = 0
c = 0

while i < n:
if not a[i] % 2:
print('No')
break

j = i

last = -1

while j < n:
if a[j] % 2 and (i - j + 1) % 2:
last = j

j += 1

if last == -1:
print('No')
break

i = last + 1

c += 1

else:
if c % 2:
print('Yes')
else:
print('No')