solve = [0, 0]

N = 10 ** 6 + 13

prime = [1 for _ in range(N+1)]
p = 2

while p * p <= N:
    if prime[p]:
        for i in range(p * p, N+1, p):
            prime[i] = 0

    p += 1

for p in range(2, N+1):
    solve.append(solve[-1])

    if prime[p]:
        solve[-1] += p
        solve[-1] %= 10

for _ in range(int(input())):
    n = int(input())
    print(solve[n])
