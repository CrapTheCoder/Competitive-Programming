for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))
    d = sorted(map(int, input().split()))

    print('AAYUSHI' if a[-1] + a[-2] > d[-1] + d[-1] else 'DAKSH')