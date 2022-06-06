for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
    s = set()
 
    d = []
 
    for i in a:
        if i in s:
            continue
 
        d.append(i)
        s.add(i)
 
    print(*d)