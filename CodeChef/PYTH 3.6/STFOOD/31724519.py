for _ in range(int(input())):
    n = int(input())
    spv = []
    
    for i in range(n):
        spv.append(tuple(map(int, input().split())))
    
    p = []
    
    for i in range(n):
        p.append(spv[i][1] // (spv[i][0] + 1) * spv[i][2])
    
    print(max(p))
