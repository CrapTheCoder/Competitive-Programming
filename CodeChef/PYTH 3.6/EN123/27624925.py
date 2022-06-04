for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    print('YES' if sum(a) <= k else 'NO')
