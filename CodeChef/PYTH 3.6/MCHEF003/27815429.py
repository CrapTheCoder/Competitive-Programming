n = int(input())

s = 0

for i in range(1, n+1):
    s += bin(i).count('1')

print(s)