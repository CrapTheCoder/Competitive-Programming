for _ in range(int(input())):
    n = int(input())
    print('Yes' if sum(list(map(int, input().split()))) % n == 0 else 'No')