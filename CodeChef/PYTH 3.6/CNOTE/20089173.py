for _ in range(int(input())):
    x, y, k, n = map(int, input().split())
    r = x - y
    
    pages = []
    costs = []
    
    for i in range(n):
        p, c = map(int, input().split())
        pages.append(p)
        costs.append(c)

    for p, c in zip(pages, costs):
        if p >= r and c <= k:
            print('LuckyChef')
            break
    else:
        print('UnluckyChef')