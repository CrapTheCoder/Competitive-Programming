for _ in range(int(input())):
    a, b = map(int, input().split())
    print('cannot distribute' if a < b or b == 0 else a // b)