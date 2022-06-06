for _ in range(int(input())):
n = int(input())
s = list(input())
t = list(input())

l = []

for i in range(n):
if s[i] != t[i]:
l.append(i)

if len(l) != 2:
print('No')
else:
s[l[0]], t[l[1]] = t[l[1]], s[l[0]]

if s == t:
print('Yes')
else:
print('No')