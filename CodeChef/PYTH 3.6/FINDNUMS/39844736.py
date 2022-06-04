s, p, k = map(int, input().split())
sol = []

def solve(n, path=()):
    if len(path) > k:
        return False

    if n == 1 and sum(path) == s and len(path) == k:
        return True

    for i in range(1, int(p ** 0.5) + 1):
        if n % i == 0:
            poss = solve(n // i, path + (i,))
            if poss:
                sol.append(i)
                return True

            if n // i != i:
                poss = solve(i, path + (n // i,))
                if poss:
                    sol.append(n // i)
                    return True

    return False

solve(p)

if not sol:
    print('NO')
else:
    print(*sorted(sol))