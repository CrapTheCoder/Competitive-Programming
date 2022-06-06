for _ in range(int(input())):
n = int(input())
s = input()

l = ''

for i in s:
if int(i) % 2:
l += i

if len(l) < 2:
print(-1)
else:
print(l[:2])