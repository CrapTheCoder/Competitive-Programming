for _ in range(int(input())):
s = input()
m = 0

for i in range(10):
for j in range(10):
c = i
t = 0

for k in s:
if k == str(c):
t += 1

if c == j:
c = i
else:
c = j

if t % 2 and i != j:
t -= 1

m = max(m, t)

print(len(s) - m)