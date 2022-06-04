from math import sqrt, floor

x = int(input())
y = x * 2
z = floor(sqrt(y))

print(z - (z * (z + 1) / 2 > x))