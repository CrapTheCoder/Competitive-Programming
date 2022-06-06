input()
tests = map(int, input().split())
 
for n in tests:
    if n < 15:
        print('NO')
        continue
 
    if any((n - i) % 14 == 0 for i in range(1, 7)):
        print('YES')
    else:
        print('NO')