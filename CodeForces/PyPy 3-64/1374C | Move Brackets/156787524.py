for _ in range(int(input())):
    n = int(input())
    s = input()
 
    mini = 0
 
    c = 0
    for i in s:
        if i == '(':
            c += 1
        else:
            c -= 1
 
        mini = min(mini, c)
 
    print(-mini)