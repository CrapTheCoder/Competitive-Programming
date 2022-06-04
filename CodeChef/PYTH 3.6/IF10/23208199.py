for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    print(sum(i >= n // 2 for i in a))
