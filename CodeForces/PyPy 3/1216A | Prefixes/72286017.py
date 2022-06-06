n = int(input())
s = list(input())

c = 0

for i in range(0, n, 2):
if s[i] == s[i+1]:
if s[i] == 'a':
s[i] = 'b'
else:
s[i] = 'a'

c += 1

print(c)
print(*s, sep='')