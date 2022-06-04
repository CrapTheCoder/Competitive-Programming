for _ in range(int(input())):
    l = list(map(int, input().split()))
    ac = sorted([l[i], l[i + 3]] for i in range(3))

    a = [ac[i][0] for i in range(3)]
    c = [ac[i][1] for i in range(3)]

    if ((a[0] < a[1] and c[0] < c[1]) or (a[0] == a[1] and c[0] == c[1])) \
        and ((a[1] < a[2] and c[1] < c[2]) or (a[1] == a[2] and c[1] == c[2])):
            print('FAIR')
    else:
        print('NOT FAIR')
