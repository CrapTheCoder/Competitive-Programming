for _ in range(int(input())):
    n, x = map(int, input().split())
    x -= 1
 
    c = [0] * n
 
    for i in range(n-1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
 
        c[u] += 1
        c[v] += 1
 
    if c[x] == 1 or n == 1 or n % 2 == 0:
        print('Ayush')
    else:
        print('Ashish')