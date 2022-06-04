for _ in range(int(input())):
    n = int(input())
    c = list(map(int, input().split()))
 
    a = [float('-inf')] + sorted(i for i in c if i % 2 == 0)
    b = [float('-inf')] + sorted(i for i in c if i % 2 == 1)
 
    at = bt = 0
 
    t = 0
    while (len(a) > 1) or (len(b) > 1):
        if t == 0:
            if a[-1] > b[-1]:
                at += a.pop()
            else:
                b.pop()
 
        else:
            if a[-1] < b[-1]:
                bt += b.pop()
            else:
                a.pop()
 
        t ^= 1
 
    if at > bt:
        print('Alice')
    if at == bt:
        print('Tie')
    if at < bt:
        print('Bob')