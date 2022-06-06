a, b, x = map(int, input().split())

new = ''

if a > b:
for i in range(x - 1):
if i % 2:
new += '1'
b -= 1
else:
new += '0'
a -= 1

else:
for i in range(1, x):
if i % 2:
new += '1'
b -= 1
else:
new += '0'
a -= 1

if new and new[-1] == '1':
new += '0' * a
new += '1' * b

else:
new += '1' * b
new += '0' * a

print(new)