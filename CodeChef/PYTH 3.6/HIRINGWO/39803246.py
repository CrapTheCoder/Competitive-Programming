def solve(i=0):
    if i == len(pfs):
        return sum(a)

    mini = float('inf')
    for j in range(k):
        a[j] *= pfs[i]
        mini = min(mini, solve(i+1))
        a[j] //= pfs[i]

    return mini

for _ in range(int(input())):
    k, x = map(int, input().split())
    ox = x

    pfs = []

    for i in range(2, int(x ** 0.5) + 1):
        c = 0
        while x % i == 0:
            x //= i
            c += 1

        if c > 0:
            pfs.append(i ** c)

    if x > 1:
        pfs.append(x)

    if len(pfs) <= k:
        print(sum(pfs) + k - len(pfs))
        continue

    a = [1] * k
    print(solve())
