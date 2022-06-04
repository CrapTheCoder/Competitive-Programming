# Author: alexwice

def solve(A):
    def to_binary(arr):
        return int(''.join(map(str, arr)).zfill(1), 2)

    N = len(A)
    ans = 0
    for n in range(1, N):
        # how many repeating with n digits?
        count = [0] * (n + 1)
        for d in range(1, n):
            if n % d: continue
            cand = (1 << (d - 1))
            for e in range(1, d):
                if d % e == 0:
                    cand -= count[e]
            count[d] = cand
        ans += sum(count)
        # print ("c", n, sum(count), count)

    n = N  # how many repeating with N digits, <= A
    count = [0] * (n + 1)
    for d in range(1, n):
        if n % d: continue

        B = to_binary(A[1: d])
        if d == 1:
            eways = 0
        else:
            eways = B
            # eg. [1,1,1]
            # we have 100 101 110 plus special 111
        if A[:d] * (n // d) <= A:
            eways += 1
        # print("!e", d, eways)
        for e in range(1, d):
            if d % e == 0:
                eways -= count[e]
        count[d] = eways
    ans += sum(count)
    return ans


def f(X):
    if X == 0: return 0
    if X == 1: return 0
    A = list(map(int, bin(X)[2:]))
    return solve(A)


x, y = map(int, input().split())
print(f(y) - f(x - 1))
