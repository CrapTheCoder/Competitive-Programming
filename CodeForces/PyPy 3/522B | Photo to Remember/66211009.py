n = int(input())

sw = 0
ws = []

m1, m1i = -1, -1
m2, m2i = -1, -1

for i in range(n):
w, h = map(int, input().split())

ws.append(w)

sw += w

if h >= m1:
m2, m2i = m1, m1i
m1, m1i = h, i

elif h >= m2:
m2, m2i = h, i

for i in range(n):
w = sw - ws[i]

print((m2 if i == m1i else m1) * w, end=' ')