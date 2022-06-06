for _ in range(int(input())):
a, b = map(int, input().split())

if a == b:
print(0)
continue

if a < b:
if (a - b) % 2 == 1:
print(1)
continue

if (a - b) % 2 == 0:
print(2)

if a > b:
if (a - b) % 2 == 0:
print(1)
continue

if (a - b) % 2 == 1:
print(2)