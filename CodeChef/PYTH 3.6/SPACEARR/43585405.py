for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))
    
    for i in range(n):
        if a[i] > i+1:
            print('Second')
            break
    else:
        s = t = 0
    
        for j, i in enumerate(a, 1):
            s += i
            t += j
    
        else:
            if s > t:
                print('Second')
                continue
    
            if (t - s) % 2:
                print('First')
            else:
                print('Second')
