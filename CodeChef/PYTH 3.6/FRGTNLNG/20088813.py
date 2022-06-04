for _ in range(int(input())):
    n, k = map(int, input().split())
    d1 = input().split()
    d2 = []

    for e in range(k):
        d2.extend(input().split()[1:])

    print(' '.join('YES' if i in d2 else 'NO' for i in d1))