n = int(input())
s = input()

t = [[0] * n for _ in range(n)]

for i in range(n):
    t[i][i] = 1

for i in range(n - 1, -1, -1):
    for j in range(i+1, n):
        if s[i] == s[j]:
            if j - i + 1 > 2:
                if t[i+1][j-1]:
                    t[i][j] = t[i+1][j-1] + 1
            else:
                t[i][j] = 1

m = 1
x, y = 0, 0

for i in range(n):
    for j in range(i+1, n):
        if t[i][j] > m:
            m = t[i][j]
            x, y = i, j

print(m * 2 - (y - x + 1) % 2)
print(s[x:y+1])