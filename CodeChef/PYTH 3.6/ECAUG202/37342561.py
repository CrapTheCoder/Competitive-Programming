for _ in range(int(input())):
    n = int(input())

    print(sum(i for i in list(map(int, input().split())) if i % 2 == 0))