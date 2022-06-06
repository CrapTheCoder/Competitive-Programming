n, m = map(int, input().split())
d = [i for i in range(1, m + 1)]
s = []

for i in range(n):
n1, n2 = map(int, input().split())

for i in range(n1, n2 + 1):
if i not in s:
s.append(i)

lis = []

for i in d:
if i not in s:
lis.append(i)

print(len(lis))
print(' '.join(str(i) for i in lis))