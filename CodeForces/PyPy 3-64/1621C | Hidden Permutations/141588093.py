def query(i):
    print(f'? {i+1}', flush=True)
    return int(input()) - 1
 
for _ in range(int(input())):
    n = int(input())
 
    p = [-1] * n
    for i in range(n):
        if p[i] == -1:
            cur = query(i)
            while p[cur] == -1:
                p[cur] = cur = query(i)
 
    print('!', *[i+1 for i in p], flush=True)