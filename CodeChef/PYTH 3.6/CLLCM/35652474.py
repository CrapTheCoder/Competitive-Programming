for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    if any(i % 2 == 0 for i in a):
        print('NO')
    else:
        print('YES')