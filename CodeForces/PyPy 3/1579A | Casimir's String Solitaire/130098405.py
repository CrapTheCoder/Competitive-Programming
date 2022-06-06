for _ in range(int(input())):
    s = input()
    a, b, c = [s.count('A'), s.count('B'), s.count('C')]
 
    if b == a + c:
        print('YES')
    else:
        print('NO')