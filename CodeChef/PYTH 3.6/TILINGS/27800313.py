n = int(input())

f = [0] * (n+1)
g = [0] * (n+1)

f[0], f[1], f[2] = 1, 1, 2
g[1], g[2] = 1, 2

for i in range(3, n+1):
    f[i] = (f[i-1] + f[i-2] + 2 * g[i-2]) % 10000
    g[i] = (g[i-1] + f[i-1]) % 10000

print(f[-1])
