for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
 
    sq = []
 
    for i in range(n):
        for j in range(n):
            while (a[i] < b[i]) and (a[j] > b[j]):
                a[i] += 1
                a[j] -= 1
                sq.append(f'{j+1} {i+1}')
 
    if a != b:
        print(-1)
    else:
        print(len(sq))
        if sq:
            print(*sq, sep='\n')