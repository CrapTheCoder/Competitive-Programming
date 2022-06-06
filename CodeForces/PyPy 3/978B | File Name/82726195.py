n = int(input())
s = input()

c = 0

while 'xxx' in s:
i = s.index('xxx')
s = list(s)
del s[i]
s = ''.join(s)

c += 1

print(c)