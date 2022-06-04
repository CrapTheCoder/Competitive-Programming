# https://www.geeksforgeeks.org/smallest-window-contains-characters-string/
from collections import defaultdict

MAX_CHARS = 256

def solve(strr):
    n = len(strr)

    dist_count = len(set([x for x in strr]))

    curr_count = defaultdict(lambda: 0)
    count = 0
    start = 0
    min_len = n

    start_index = 0

    for j in range(n):
        curr_count[strr[j]] += 1

        if curr_count[strr[j]] == 1:
            count += 1

        if count == dist_count:
            while curr_count[strr[start]] > 1:
                if curr_count[strr[start]] > 1:
                    curr_count[strr[start]] -= 1

                start += 1

            len_window = j - start + 1

            if min_len > len_window:
                min_len = len_window
                start_index = start

    return str(strr[start_index: start_index + min_len])

for _ in range(int(input())):
    x = solve(input().strip())

    print(''.join(str(ord(c) - ord('a') + 1) for c in x))
