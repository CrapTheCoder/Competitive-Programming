n = int(input())
s = 0

for i in range(1, n+1):
    if i % 2:
        s += i * i
    else:
        s += 2 * i * i

if s % 2:
    print('Jhon')
else:
    print('Ravi')