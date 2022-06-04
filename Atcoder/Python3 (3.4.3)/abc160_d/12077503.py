n, x, y = map(int, input().split())
x -= 1
y -= 1

dists = [0] * (n-1)

for i in range(n):
    for j in range(i+1, n):
        d = min(
            abs(j-i),
            abs(i-x) + abs(y-j) + 1,
            abs(i-y) + abs(x-j) + 1
        )

        dists[d-1] += 1

print(*dists, sep='\n')