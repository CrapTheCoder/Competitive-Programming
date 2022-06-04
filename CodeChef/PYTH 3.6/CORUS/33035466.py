def main():
    from sys import stdin
    from collections import Counter

    input = stdin.readline

    for _ in range(int(input())):
        n, q = map(int, input().split())
        s = Counter(input().strip())

        for _ in range(q):
            k = int(input())

            print(sum(s[i] - k for i in s if s[i] > k))

main()