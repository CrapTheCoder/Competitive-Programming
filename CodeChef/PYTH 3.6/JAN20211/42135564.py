for _ in range(int(input())):
    n = int(input())
    print('Magical' if bin(n).count('1') % 2 == 0 else 'Non-Magical')