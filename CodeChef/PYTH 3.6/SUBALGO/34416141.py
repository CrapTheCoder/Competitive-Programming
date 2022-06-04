n, a = map(int, input().split())
n = str(n)

for _ in range(a):
    if n == '0':
        break

    if n[-1] == '0':
        n = n[:-1]
    else:
        n = str(int(n) - 1)

print(n)
