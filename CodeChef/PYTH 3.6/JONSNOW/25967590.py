for _ in range(int(input())):
    n, m = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if sum(a) < sum(b):
        print('Death')
    else:
        print('Snow')
