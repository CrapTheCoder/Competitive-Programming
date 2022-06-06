n = int(input())
c = 0
i = 1

while n > 0:
n -= i
i *= 2
c += 1

print(c)