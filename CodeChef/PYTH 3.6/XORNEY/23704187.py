def xor(n):
    if n % 4 == 0: return n
    if n % 4 == 1: return 1
    if n % 4 == 2: return n+1
    if n % 4 == 3: return 0

for _ in range(int(input())):
    l, r = map(int, input().split())
    
    if (xor(r) ^ xor(l-1)) % 2:
        print('Odd')
    else:
        print('Even')