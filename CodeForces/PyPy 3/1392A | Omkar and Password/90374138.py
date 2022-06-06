for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
    if len(list(set(a))) == 1:
        print(n)
        continue
 
    print(1)