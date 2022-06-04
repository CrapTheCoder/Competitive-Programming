n = int(input())
x = int(input(), 2)

c = 0

while x % 2 ** c == 0:
    c += 1

print(c - 1)