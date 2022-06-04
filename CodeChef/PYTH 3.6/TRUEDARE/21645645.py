for _ in range(int(input())):
    tr = int(input())
    lt1 = set(map(int, input().split()))
    dr = int(input())
    ld1 = set(map(int, input().split()))

    ts = int(input())
    lt2 = set(map(int, input().split()))
    ds = int(input())
    ld2 = set(map(int, input().split()))

    for i in lt2:
        if i not in lt1:
            print('no')
            break
    else:
        for i in ld2:
            if i not in ld1:
                print('no')
                break
        else:
            print('yes')