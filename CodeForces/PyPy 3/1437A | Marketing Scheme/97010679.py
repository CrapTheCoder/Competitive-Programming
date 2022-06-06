for _ in range(int(input())):
    l, r = map(int, input().split())
    print('YES' if l*2 > r else 'NO')