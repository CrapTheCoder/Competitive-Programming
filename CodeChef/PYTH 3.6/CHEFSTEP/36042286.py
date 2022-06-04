for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    print(''.join('1' if a[i] % k == 0 else '0' for i in range(n)))