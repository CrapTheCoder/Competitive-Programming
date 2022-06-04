for _ in range(int(input())):
    n, m = map(int, input().split())
    zero = n - m
    chunks = m+1

    mini = zero // chunks
    maxi = -(-zero // chunks)

    if mini == maxi:
        print(maxi * (maxi + 1) // 2 * chunks)
        continue

    x = (zero - mini * chunks) // (maxi - mini)

    # print(x, maxi, mini, chunks, zero)
    print(maxi * (maxi + 1) // 2 * x + mini * (mini + 1) // 2 * (chunks - x))
