for _ in range(int(input())):
s = input()
n = len(s)

s0 = s.count('0')
s1 = s.count('1')

ans = min(s0, s1)

p0 = p1 = 0

for i in range(n):
if s[i] == '0':
p0 += 1
s0 -= 1

if s[i] == '1':
p1 += 1
s1 -= 1

ans = min(ans, p0 + s1, p1 + s0)

print(ans)