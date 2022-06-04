for _ in range(int(input())):
    n, c = map(int, input().split())
    e = list(map(int, input().split()))
    
    print('Yes' if sum(e) <= c else 'No')