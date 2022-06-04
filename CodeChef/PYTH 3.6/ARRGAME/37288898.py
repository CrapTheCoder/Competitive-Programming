# This is basically my solution for the first problem

# p1 = player 1
# p2 = player 2

from itertools import groupby

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    # Find the length of all contiguous 0s
    t = []
    
    for i in groupby(a):
        i = list(i)
        if i[0] == 0:
            t.append(len(list(i[1])))

    t.sort()

    # If there are no 0s, then there no move to make for p1, and they lose
    if len(t) == 0:
        print('No')
        continue

    # If there is exactly 1 group of 0s, there are two cases:
    if len(t) == 1:
        # Case odd: p1 can occupy the center and win because they have 1 extra space
        if t[-1] % 2:
            print('Yes')

        # Case even: if p1 occupies any center, then p2 will do the same for the center and get one extra move. So p1 loses
        else:
            print('No')

        continue

    # Same reason as stated above for case even
    if t[-1] % 2 == 0:
        print('No')
        continue

    # p1 HAS to occupy the center, else they have less moves.
    # If p2 plays on the same group as p1, they are going to lose.
    # BUT, remember p1 has only t[-1] // 2 moves left.
    # So, if there's any other group with at least t[-1] // 2 spaces, p2 can win by selecting the end of said group and win
    if t[-1] // 2 < t[-2]:
        print('No')
        continue

    print('Yes')