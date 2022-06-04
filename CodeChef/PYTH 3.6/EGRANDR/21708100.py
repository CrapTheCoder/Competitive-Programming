for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    if (2 in a) or (5 not in a):
        print('No')
    else:
        if sum(a) / n < 4:
            print('No')
        else:
            print('Yes')