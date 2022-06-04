for _ in range(int(input())):
    n = int(input())
    a = [int(input()) for i in range(n)]
    
    for i in set(a):
        if a.count(i) % 2:
            print(i)
            break
            