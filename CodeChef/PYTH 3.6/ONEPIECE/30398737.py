MOD = 10 ** 9 + 7
MAXN = 10 ** 5 + 10

factorial = [1]

for i in range(1, MAXN + 1):
    factorial.append((factorial[-1] * i) % MOD)

def f(n):
    return (factorial[3 * n] * pow(factorial[3] ** n, MOD - 2, MOD)) % MOD

for _ in range(int(input())):
    print(f(int(input())))