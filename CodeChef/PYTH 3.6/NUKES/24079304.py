a, n, k = map(int, input().split())
n += 1

ans = []

for i in range(k):
    ans.append(a % n)
    a //= n

print(*ans)