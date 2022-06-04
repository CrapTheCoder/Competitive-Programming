for _ in range(int(input())):
    n = int(input())
    s = input()
    r = input()

    if s.count('1') != r.count('1'):
        print('NO')
    else:
        print('YES')
