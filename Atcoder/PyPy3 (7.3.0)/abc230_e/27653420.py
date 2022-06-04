n = int(input())

s = 0

i = 1
while i <= n:
    x = n // i
    ni = n // x + 1

    s += x * (ni - i)
    i = ni

print(s)