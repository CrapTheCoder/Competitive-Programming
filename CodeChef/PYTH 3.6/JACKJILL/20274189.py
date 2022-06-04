for _ in range(int(input())):
    n, k, d = map(int, input().split())
    jack = list(map(int, input().split()))
    jill = list(map(int, input().split()))

    for i in range(k, n, k):
        if sum(jack[i-k:i]) + sum(jill[i-k:i]) >= d:
            print('no')
            break
    else:
        print('yes')