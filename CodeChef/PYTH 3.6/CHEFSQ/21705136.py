for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    m = int(input())
    b = list(map(int,input().split()))

    i = 0
    j = 0

    while i < m:
        for j in range(j, n):
            if b[i] == a[j]:
                break
        else:
            print('No')
            break

        i += 1
    else:
        print('Yes')