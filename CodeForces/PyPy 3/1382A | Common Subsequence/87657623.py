for _ in range(int(input())):
    n, m = map(int, input().split())
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))
 
    print('YES\n1 ' + str(list(a.intersection(b))[0]) if a.intersection(b) else 'NO')