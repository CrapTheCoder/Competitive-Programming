from string import ascii_uppercase

for _ in range(int(input())):
    n = int(input())
    s = list(range(1, n+1))

    for i in range(n):
        print('_' * i + ascii_uppercase[:n-i])