for _ in range(int(input())):
    n = int(input())
    d = dict()

    for i in range(n):
        s = input()
        d[s] = d.get(s, 0) + 1

    if n == 0: print('Draw')
    elif n == 1: print(list(d.keys())[0])
    elif d[list(d.keys())[0]] < d[list(d.keys())[1]]: print(list(d.keys())[1])
    elif d[list(d.keys())[0]] > d[list(d.keys())[1]]: print(list(d.keys())[0])
    else: print('Draw')