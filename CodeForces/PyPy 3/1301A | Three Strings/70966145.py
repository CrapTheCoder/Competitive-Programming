for _ in range(int(input())):
    a = input()
    b = input()
    c = input()
 
    for i in range(len(a)):
        if c[i] != b[i] and a[i] != c[i]:
            print('NO')
            break
    else:
        print('YES')