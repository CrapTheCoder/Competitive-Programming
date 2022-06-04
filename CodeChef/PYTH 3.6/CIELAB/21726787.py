a, b = map(int, input().split())
c = a - b

if c % 10 == 9: print(c - 1)
if c % 10 != 9: print(c + 1)
