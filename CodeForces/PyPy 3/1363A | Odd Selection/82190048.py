for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
 
    o = sum(i % 2 for i in a)
    e = n - o
 
    print('YNeos'[(x>o - (o-1) % 2 + e) or ((o == 0) or (e == 0 and x%2 == 0))::2])