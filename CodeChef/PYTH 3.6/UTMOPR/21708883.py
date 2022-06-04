for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    print('odd' if k == 1 and (not sum(a) % 2) else 'even')