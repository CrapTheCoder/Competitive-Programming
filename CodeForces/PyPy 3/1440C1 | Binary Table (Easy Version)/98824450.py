from copy import deepcopy


def op(x1, y1, x2, y2, x3, y3, ans, a):
ans.append((x1+1, y1+1, x2+1, y2+1, x3+1, y3+1))
a[x1][y1] = 1 - a[x1][y1]
a[x2][y2] = 1 - a[x2][y2]
a[x3][y3] = 1 - a[x3][y3]


def perf(i, j, a, ans):
mat = [a[i][j], a[i][j+1], a[i+1][j], a[i+1][j+1]]

if mat == [1, 1, 1, 1]: op(i, j, i+1, j, i, j+1, ans, a)
mat = [a[i][j], a[i][j+1], a[i+1][j], a[i+1][j+1]]

if   mat == [0, 0, 0, 1]: op(i, j+1, i+1, j, i+1, j+1, ans, a)
elif mat == [0, 0, 1, 0]: op(i, j, i+1, j, i+1, j+1, ans, a)
elif mat == [0, 1, 0, 0]: op(i, j, i, j+1, i+1, j+1, ans, a)
elif mat == [1, 0, 0, 0]: op(i, j, i+1, j, i, j+1, ans, a)
mat = [a[i][j], a[i][j+1], a[i+1][j], a[i+1][j+1]]

if   mat == [1, 0, 0, 1]: op(i, j, i+1, j, i, j+1, ans, a)
elif mat == [0, 1, 1, 0]: op(i, j, i+1, j, i+1, j+1, ans, a)
mat = [a[i][j], a[i][j+1], a[i+1][j], a[i+1][j+1]]

if   mat == [1, 1, 0, 0]: op(i+1, j, i+1, j+1, i, j+1, ans, a)
elif mat == [1, 0, 1, 0]: op(i+1, j, i+1, j+1, i, j+1, ans, a)
elif mat == [0, 1, 0, 1]: op(i, j, i+1, j, i+1, j+1, ans, a)
elif mat == [0, 0, 1, 1]: op(i, j, i, j+1, i+1, j+1, ans, a)
mat = [a[i][j], a[i][j+1], a[i+1][j], a[i+1][j+1]]

if   mat == [1, 1, 1, 0]: op(i, j, i, j+1, i+1, j, ans, a)
elif mat == [1, 1, 0, 1]: op(i, j, i, j+1, i+1, j+1, ans, a)
elif mat == [1, 0, 1, 1]: op(i, j, i+1, j, i+1, j+1, ans, a)
elif mat == [0, 1, 1, 1]: op(i, j+1, i+1, j, i+1, j+1, ans, a)


def side1(a):
ans = []

for i in range(0, n-1, 2):
for j in range(0, m-1, 2):
perf(i, j, a, ans)

for i in range(n-2, -1, -2):
for j in range(m-2, -1, -2):
perf(i, j, a, ans)

for i in range(0, n-1, 2):
for j in range(m-2, -1, -2):
perf(i, j, a, ans)

for i in range(n-2, -1, -2):
for j in range(0, m-1, 2):
perf(i, j, a, ans)

return ans


for _ in range(int(input())):
n, m = map(int, input().split())
a = [list(map(int, input())) for _ in range(n)]

ans = side1(deepcopy(a))

print(len(ans))
for i in ans:
print(*i)