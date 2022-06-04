n = int(input())
a = list(map(lambda x: int(x) - 1, input().split()))

anss = []

visited = [False] * n

for i in range(n):
    if visited[i]:
        continue

    visited[i] = True

    current = i

    ans = []

    while a[current] != i:
        current = a[current]
        visited[current] = True
        ans.append(current + 1)

    anss.append([i + 1] + ans + [i + 1])

print(len(anss))

for i in anss:
    print(' '.join(str(j) for j in i))
