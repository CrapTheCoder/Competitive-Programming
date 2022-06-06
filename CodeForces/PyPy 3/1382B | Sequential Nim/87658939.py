for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
    c = 0
 
    for i in range(n):
        if a[i] != 1:
            break
 
        c += 1
 
    else:
        if c % 2 == 1:
            print('First')
        else:
            print('Second')
 
        continue
 
    if c % 2 == 0:
        print('First')
    else:
        print('Second')