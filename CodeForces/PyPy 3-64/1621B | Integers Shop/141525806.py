from sys import stdin
input = stdin.readline
 
min = lambda x, y: x if x < y else y
 
for _ in range(int(input())):
    n = int(input())
 
    sl = float('inf')
    sr = float('-inf')
    si = -1
 
    bl = float('inf')
    br = float('-inf')
 
    bli = -1
    bri = -1
 
    a = []
    for i in range(n):
        l, r, c = map(int, input().split())
        a.append((l, r, c))
 
        if l < bl:
            bl = l
            bli = i
 
        elif l == bl and c < a[bli][2]:
            bli = i
 
        if r > br:
            br = r
            bri = i
 
        elif r == br and c < a[bri][2]:
            bri = i
 
        if (l <= sl and r > sr) or (l < sl and r >= sr):
            sl, sr = l, r
            si = i
 
        elif l == sl and r == sr and c < a[si][2]:
            si = i
 
        if bl < sl or br > sr:
            print(a[bli][2] + a[bri][2])
        else:
            print(min(a[si][2], a[bli][2] + a[bri][2]))