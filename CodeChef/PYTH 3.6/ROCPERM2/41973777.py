for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(n):
        if abs(i+1 - a[i]) > 3:
            print('Yes')
            break
    else:
        print('No')