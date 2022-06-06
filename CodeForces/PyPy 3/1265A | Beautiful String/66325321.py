for _ in range(int(input())):
    s = list('_' + input() + '_')
 
    for i, j in enumerate(s):
        if s[i] == '?':
            d = {'a', 'b', 'c'}
 
            if s[i-1] in d: d.remove(s[i-1])
            if s[i+1] in d: d.remove(s[i+1])
 
            s[i] = list(d)[0]
 
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            print(-1)
            break
    else:
        print(''.join(s[1:-1]))