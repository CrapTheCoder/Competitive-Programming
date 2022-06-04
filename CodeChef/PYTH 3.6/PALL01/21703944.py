for _ in range(int(input())):
    s = input()
    print('wins' if s == s[::-1] else 'losses')