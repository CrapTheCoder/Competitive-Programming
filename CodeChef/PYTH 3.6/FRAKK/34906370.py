for _ in range(int(input())):
    n = int(input())
    p, q = map(int, input().split())
    
    print(sum(int(i) for i in str(p * (10 ** n) // q)[-n:]))