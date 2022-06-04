def main():
    from sys import stdin
    from collections import Counter

    input = stdin.readline

    for _ in range(int(input())):
        n, q = map(int, input().split())
        s = Counter(input().strip())

        for _ in range(q):
            k = int(input())

            ans = 0

            for i in s:
                if s[i] > k:
                    ans += s[i] - k

            print(ans)

main()