for _ in range(int(input())):
x, y, z = sorted(map(int, input().split()))

if x == y == z:
print('YES')
print(x, y, z)
continue

if x == y and y < z:
print('NO')
continue

if x < y and y == z:
print('YES')
print(x, x, z)
continue

print('NO')

"""

x, y, z

(a, b), (a, c), (b, c)

x y z
1 2 2



"""