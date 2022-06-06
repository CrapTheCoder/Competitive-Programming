s = input()

if not '[' in s or not ']' in s:
print(-1)

else:
a = s.index('[')
b = len(s) - s[::-1].index(']') - 1

s = s[a:b+1]

if s.count(':') < 2:
print(-1)
else:
a = s.index(':')
b = len(s) - s[::-1].index(':') - 1

s = s[a:b+1]

print(s.count('|') + 4)