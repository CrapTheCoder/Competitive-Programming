for _ in range(int(input())):
    a, b = sorted(map(int, input().split()))
 
    if a == b == 1:
        print(0)
        continue
 
    if a == b == 2:
        print(2)
        continue
 
    if a == 1 and b == 2:
        print(1)
        continue
 
    s = (b // 3) * a + (a // 3) * (b % 3)
    a, b = sorted((a%3, b%3))
 
    if a == 0 or b == 0:
        print(s)
        continue
 
    if a == b == 1:
        print(s+1)
        continue
 
    if a == b == 2:
        print(s+2)
        continue
 
    print(s+1)