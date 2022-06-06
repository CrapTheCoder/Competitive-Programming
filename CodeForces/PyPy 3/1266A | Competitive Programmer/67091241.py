for _ in range(int(input())):
s = input()

if not s.strip('0'):
print('red')
continue

if len(s) == 2:
if s == '06' or s == '60':
print('red')
else:
print('cyan')

continue

if '0' in s:
s = s.replace('0', '', 1)

if (sum(int(i) for i in s) % 3 == 0) and (any(int(i) % 2 == 0 for i in s)):
print('red')
else:
print('cyan')

else:
print('cyan')