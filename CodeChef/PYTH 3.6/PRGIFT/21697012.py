for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    even = 0

    for i in a:
        even += not i % 2

    if even >= k:
        if k == 0 and even == n:
            print('NO')
        else:
            print('YES')
    else:
        print('NO')