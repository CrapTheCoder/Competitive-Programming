for _ in range(int(input())):
    n = int(input())

    print(bin(n).count('1') - 1)