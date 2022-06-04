for _ in range(int(input())):
    input()
    s = str(input())
    c = s.count('1')
    print(c * (c + 1) // 2)