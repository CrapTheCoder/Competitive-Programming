def next_permutation(a, n):
    for i in range(n - 2, -1, -1):
        if a[i] < a[i+1]:
            break
    else:
        return False

    j = next(j for j in range(n-1, i, -1) if a[i] < a[j])

    a[i], a[j] = a[j], a[i]
    a[i+1:] = a[i+1:][::-1]

    return True

n, k = map(int, input().split())

for _ in range(k):
    a = list(map(int, input().split()))
    next_permutation(a, n)

    print(*a)
