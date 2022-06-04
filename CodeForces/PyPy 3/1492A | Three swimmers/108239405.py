for _ in range(int(input())):
    p, a, b, c = map(int, input().split())
 
    mini = float('inf')
    for a in [a, b, c]:
        mini = min(mini, (-(-p // a) * a) - p)
 
    print(mini)