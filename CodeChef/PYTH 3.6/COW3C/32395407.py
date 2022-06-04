MOD = 10 ** 9 + 7
SIZE = 500000

n = int(input())

a = [0] * (2 * SIZE + 100)

for _ in range(n):
    b, d = map(int, input().split())

    b += SIZE
    d += SIZE

    a[b] += 1
    a[d+1] -= 1

for i in range(1, len(a)):
    a[i] += a[i-1]

print(sum(a) % MOD)