for _ in range(int(input())):
    s = ''.join(sorted(input()))
    t = input()
 
    if 'a' not in s or 'b' not in s or 'c' not in s:
        print(s)
        continue
 
    if t == 'abc':
        s = ''.join(sorted(s.replace('c', '~').replace('b', 'c').replace('~', 'b')))
        s = s.replace('c', '~').replace('b', 'c').replace('~', 'b')
        print(s)
    else:
        print(s)