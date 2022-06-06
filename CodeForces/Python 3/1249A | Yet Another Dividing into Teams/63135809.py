for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))
 
    for i in range(n - 1):
        if a[i+1] - a[i] == 1:
            print(2)
            break
    else:
        print(1)