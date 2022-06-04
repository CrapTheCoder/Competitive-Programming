for i in range(int(input())):
    n = int(input())
    print(2 ** (len(bin(n)[2:]) - 1))