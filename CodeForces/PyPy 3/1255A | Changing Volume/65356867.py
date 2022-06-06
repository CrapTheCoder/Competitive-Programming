for _ in range(int(input())):
    a, b = map(int, input().split())
    c = abs(a - b)
 
    if c % 5 in [1, 2]:
        print(c // 5 + 1)
    elif c % 5 in [3, 4]:
        print(c // 5 + 2)
    else:
        print(c // 5)