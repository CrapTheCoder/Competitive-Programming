def query(i):
    if a[i] != -1:
        return a[i]
 
    print('?', i, flush=True)
    a[i] = int(input())
    return a[i]
 
 
def check(i):
    if query(i-1) < query(i):
        return True
 
    if query(i) > query(i+1):
        return False
 
    print('!', i, flush=True)
    exit()
 
 
n = int(input())
a = [-1] * (n+2)
a[0] = a[-1] = float('inf')
 
l, r = 1, n
 
while l <= r:
    m = (l + r) // 2
 
    if check(m):
        r = m-1
    else:
        l = m+1