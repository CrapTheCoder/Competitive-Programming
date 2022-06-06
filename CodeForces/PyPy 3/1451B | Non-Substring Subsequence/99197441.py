for _ in range(int(input())):
n, q = map(int, input().split())
s = input()

for _ in range(q):
l, r = map(int, input().split())
l -= 1
r -= 1

t = s[l:r+1]

flag = False

for i in range(l):
if s[i] == t[0]:
flag = True
break

for i in range(r+1, n):
if s[i] == t[-1]:
flag = True
break

if flag:
print('YES')
else:
print('NO')