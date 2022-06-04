for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    j, s = 1, a[0]
    print(a[0], end=' ')

    for i in a[1:]:
        if i != -1:
            print(i, end=' ')
            s += i
        else:
            print(s // j, end=' ')
            s += s // j
        j += 1
    print()
