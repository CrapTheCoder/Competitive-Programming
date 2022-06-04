for _ in range(int(input())):
    l = sorted(map(int, input().split()))

    print('YES' if l[0] == l[1] and l[2] == l[3] else 'NO')