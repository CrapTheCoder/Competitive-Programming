for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
    if n == 1:
        if a[0] % 2:
            print(-1)
        else:
            print(1)
            print(1)
 
        continue
 
    if a[0] % 2 == 0:
        print(1)
        print(1)
        continue
 
    if a[1] % 2 == 0:
        print(1)
        print(2)
        continue
 
    print(2)
    print(1, 2)