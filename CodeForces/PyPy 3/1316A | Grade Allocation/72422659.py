for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
 
    avg = sum(a) / n
 
    print(min(m, sum(a)))