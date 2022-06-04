from string import ascii_lowercase

def main():
    from sys import stdin
    from collections import Counter

    input = stdin.readline

    for _ in range(int(input())):
        n, q = map(int, input().split())
        s = Counter(input().strip())

        for _ in range(q):
            k = int(input())
            print(sum(s[i] - k for i in ascii_lowercase if s[i] > k))

main()