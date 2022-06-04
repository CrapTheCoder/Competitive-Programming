for _ in range(int(input())):
    n, p = map(int, input().split())
    a = list(map(int, input().split()))

    easy = 0
    hard = 0

    for i in a:
        if i >= p // 2:
            easy += 1
        if i <= p // 10:
            hard += 1

    if [easy, hard] == [1, 2]:
        print('yes')
    else:
        print('no')