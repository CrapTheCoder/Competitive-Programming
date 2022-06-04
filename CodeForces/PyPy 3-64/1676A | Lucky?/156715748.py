for _ in range(int(input())):
    n = input()
    print('YES' if int(n[0]) + int(n[1]) + int(n[2]) == int(n[-1]) + int(n[-2]) + int(n[-3]) else 'NO')