for _ in range(int(input())):
    n, m = map(int, input().split())
    c = sum(map(int, input().split()))
    w = sum(map(int, input().split()))

    if w > c:
        print('Death')
    else:
        print('Snow')