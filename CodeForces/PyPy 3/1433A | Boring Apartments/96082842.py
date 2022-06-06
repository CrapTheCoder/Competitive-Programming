for _ in range(int(input())):
x = int(input())

c = 0
for i in range(1, 10):
k = i

while i <= 10000:
c += len(str(i))

if i == x:
break

i *= 10
i += k

else:
continue

break

print(c)