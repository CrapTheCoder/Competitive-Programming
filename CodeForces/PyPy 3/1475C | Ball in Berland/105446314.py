for _ in range(int(input())):
    a, b, k = map(int, input().split())
    aa = list(map(int, input().split()))
    bb = list(map(int, input().split()))
    c = 0
 
    da = [0] * a
    db = [0] * b
 
    for i in range(k):
        da[aa[i]-1] += 1
        db[bb[i]-1] += 1
 
        c += i - da[aa[i] - 1] - db[bb[i] - 1] + 2
 
    print(c)