for _ in range(int(input())):
n = int(input())
s = input()

c0 = c1 = 0

for i in s:
if i == '1':
break
c0 += 1

for i in s[::-1]:
if i == '0':
break
c1 += 1

if c0 + c1 == n:
print(s)
continue

print('0' * c0 + '0' + '1' * c1)