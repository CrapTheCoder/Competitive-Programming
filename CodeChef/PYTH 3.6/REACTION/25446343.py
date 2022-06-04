for _ in range(int(input())):
    r, c = map(int, input().split())
    
    a = 0
    
    for i in range(r):
        l = list(map(int, input().split()))
        
        for j in range(c):
            if (i == j == 0) or (i == 0 and j == c-1) or (i == r-1 and j==0) or (i == r-1 and j == c-1):
                if l[j] >= 2:
                    a = 1
                    break
            elif 0 < i < r-1 and 0 < j < c - 1:
                if l[j] >= 4:
                    a = 1
                    break
            else:
                if l[j] >= 3:
                    a = 1
                    break

    print(['Stable', 'Unstable'][a])