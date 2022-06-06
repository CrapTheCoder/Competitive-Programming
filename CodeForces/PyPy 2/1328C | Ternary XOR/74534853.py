from sys import stdin
raw_input = stdin.readline
 
#Author: sarthakmanna
 
for tc in xrange(input()):
    N = input()
    S = list(raw_input())
 
    A, B = [], []
    f = 0
 
    for i in xrange(N):
        d = int(S[i])
 
        if f:
            A.append(str(d))
            B.append('0')
        else:
            d1 = d / 2
            d2 = d - d1
            if d1 < d2: f = True
            A.append(str(d1))
            B.append(str(d2))
 
    print ''.join(A)
    print ''.join(B)