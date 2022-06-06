for _ in range(int(input())):
n = int(input())

t = []

while n:
n, r = divmod(n, 3)
t.append(str(r))

t = ['0'] + t[::-1]

if '2' in t:
ind = t.index('2')

i = 0

for i in range(ind, -1, -1):
if t[i] == '0':
t[i] = '1'
break
else:
t[i] = '0'

t[ind:] = '0' * (len(t[ind:]))

t = ''.join(t)

print(int(t, 3))