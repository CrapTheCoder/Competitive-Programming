V = 'aeiou'
 
s1, s2 = input(), input()
n1, n2 = len(s1), len(s2)
 
if n1 != n2:
    print('No')
else:
    for i in range(n1):
        if (s1[i] in V) != (s2[i] in V):
            print('No')
            break
    else:
        print('Yes')