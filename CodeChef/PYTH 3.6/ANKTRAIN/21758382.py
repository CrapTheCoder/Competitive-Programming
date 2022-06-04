l = [-1, 'LB', 'MB', 'UB']

for _ in range(int(input())):
    b = int(input())
    e = b % 8

    if e == 0: print(b-1, 'SL', sep='')
    elif e <= 3: print(b+3, l[e], sep='')
    elif e < 7: print(b-3, l[e-3], sep='')
    elif e == 7: print(b+1, 'SU', sep='')
