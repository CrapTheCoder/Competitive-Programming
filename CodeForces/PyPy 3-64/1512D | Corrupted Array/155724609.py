for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))
 
    if sum(a[:-2]) in a[-2:]:
        print(*a[:-2])
 
    elif sum(a[:-1]) - a[-1] in a:
        a.remove(sum(a[:-1]) - a[-1])
 
        if sum(a[:-1]) == a[-1]:
            print(*a[:-1])
        else:
            print(-1)
 
    else:
        print(-1)