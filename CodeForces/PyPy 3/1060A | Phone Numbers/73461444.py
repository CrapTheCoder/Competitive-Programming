n = int(input())
s = input()

c = 0

for i in range(s.count('8')):
n -= 11

if n < 0:
break

c += 1

print(c)