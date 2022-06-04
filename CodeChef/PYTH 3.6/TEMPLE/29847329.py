from math import factorial

MOD = 10 ** 9 + 7

h = int(input())
a, b, c = map(int, input().split())
k = int(input())

def solve(t, f=k, m=0):
    if m == 3:
        if f == 0:
            yield t

        return

    m += 1

    for i in range(f+1):
        yield from solve(t + (i,), f - i, m)

s = 0

for x, y, z in solve(()):
    if x * a + y * b + z * c == h:
        s += factorial(k) // (factorial(x) * factorial(y) * factorial(z))

print(s % MOD)