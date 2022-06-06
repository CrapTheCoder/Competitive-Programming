for _ in range(int(input())):
    s = input()
 
    ab = s.count('ab')
    ba = s.count('ba')
 
    if ab == ba:
        print(s)
        continue
 
    s1 = 'a' + s[1:]
    s2 = 'b' + s[1:]
    s3 = s[:-1] + 'a'
    s4 = s[:-1] + 'b'
 
    for s in [s1, s2, s3, s4]:
        ab = s.count('ab')
        ba = s.count('ba')
 
        if ab == ba:
            print(s)
            break