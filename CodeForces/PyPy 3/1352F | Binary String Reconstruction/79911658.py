for _ in range(int(input())):
    n0, n1, n2 = map(int, input().split())
 
    if n1 == 0 and n2 == 0:
        print('0' * (n0+1))
        continue
 
    if n0 == 0 and n1 == 0:
        print('1' * (n2+1))
        continue
 
    if n0 == 0 and n2 == 0:
        print('01' * (n1 // 2) + '01'[:n1%2+1])
        continue
 
    if n0 == 0:
        print('01' * (n1 // 2 + n1 % 2) + '1' * n2 + '0' * (not n1 % 2))
        continue
 
    if n1 == 0:
        raise ValueError('Impossible to create')
 
    if n2 == 0:
        print('10' * (n1 // 2 + n1 % 2) + '0' * n0 + '1' * (not n1 % 2))
        continue
 
    print('0' * n0 + '01' * (n1 // 2 + n1 % 2) + '1' * n2 + '0' * (not n1 % 2))