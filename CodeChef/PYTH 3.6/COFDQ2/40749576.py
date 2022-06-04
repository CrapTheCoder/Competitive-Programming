m, n = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(m)]

m, n = len(A), len(A[0])
for i in range(m):
    if A[i][0] == 0:
        for j in range(n): A[i][j] ^= 1

for j in range(n):
    cnt = sum(A[i][j] for i in range(m))
    if cnt < m - cnt:
        for i in range(m): A[i][j] ^= 1

print(sum(int("".join(map(str, A[i])), 2) for i in range(m)))