for i in range(int(input())):
    l, k = map(int, input().split())
    n = l - k + 1
    
    print(f'Case {i+1}', end=': ')
    print(n * (n + 1) // 2 if l >= k else 0)