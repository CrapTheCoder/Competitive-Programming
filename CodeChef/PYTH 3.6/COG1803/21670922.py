for _ in range(int(input())):
    n = int(input())
    l = input().split()

    x = 0

    for i in l:
        x += int(i)

    if x < 0:
        print('NO')
    else:
        print('YES')
