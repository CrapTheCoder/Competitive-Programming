def f(mid, ar, n, m):
    c = s = 0

    for i in range(n):
        if ar[i] > mid:
            return False

        s += ar[i]

        if s > mid:
            c += 1
            s = ar[i]

    c += 1

    if c <= m:
        return True

    return False

def solve(ar, n, m):
    st, en = 1, 0

    for i in range(n):
        en += ar[i]

    a = 0
    while st <= en:
        mid = (st + en) // 2

        if f(mid, ar, n, m):
            a = mid
            en = mid - 1
        else:
            st = mid + 1

    return a

for _ in range(int(input())):
    n = int(input())
    ar = list(map(int, input().split()))
    m = int(input())

    print(solve(ar, n, m))