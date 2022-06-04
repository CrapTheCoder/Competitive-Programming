from string import ascii_uppercase

for _ in range(int(input())):
    n = int(input())

    for i in range(n):
        print((n-i-1) * ' ', end='')
        print(ascii_uppercase[i] * (i+1) + str(i+1) * (i+1), end='')
        print((n-i-1) * ' ', end='')
        print()