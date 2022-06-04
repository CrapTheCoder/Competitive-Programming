x = int(input())

s = 100
c = 0

while s < x:
    s += s // 100
    c += 1

print(c)