def solve():
    for a in '()':
        for b in '()':
            for c in '()':
                t = s.replace('A', a).replace('B', b).replace('C', c)
 
                c = 0
                for i in t:
                    if i == '(':
                        c += 1
                    else:
                        c -= 1
 
                    if c < 0:
                        break
 
                else:
                    if c == 0:
                        print('YES')
                        return
 
    print('NO')
 
for _ in range(int(input())):
    s = input().strip()
 
    solve()