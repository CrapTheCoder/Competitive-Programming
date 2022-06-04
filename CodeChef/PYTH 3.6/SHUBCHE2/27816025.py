z = int(input())

x = z - 1
y = z + 1

while x ^ z != x + z:
    x -= 1

y = z + 1

while y ^ z != y + z:
    y += 1

print(x, y)