def solve():
    x = a[0] * a[-1]

    vec = []
    i = 2
    while i * i <= x:
        if x % i == 0:
            vec.append(i)
            if (x // i) != i:
                vec.append(x // i)
        i += 1

    vec.sort()

    if len(vec) != n:
        return -1
    else:
        j = 0
        for it in range(n):
            if a[j] != vec[it]:
                return -1
            else:
                j += 1

    return x

for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))

    print(solve())
