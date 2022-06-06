for _ in range(int(input())):
    n = int(input())
    s = input()
 
    a = ''
    b = ''
 
    for i in range(n):
        if s[i] == '1':
            a += '0'
            b += '1'
 
            for i in range(i+1, n):
                a += s[i]
                b += '0'
 
            break
 
        else:
            if s[i] == '0':
                a += '0'
                b += '0'
            else:
                a += '1'
                b += '1'
 
    print(b)
    print(a)