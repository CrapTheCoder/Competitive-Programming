x = y = z = 0

for i in range(int(input())):
xi, yi, zi = map(int, input().split())

x += xi
y += yi
z += zi

print('YES' if x == y == z == 0 else 'NO')