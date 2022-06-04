for _ in range(int(input())):
    n = int(input())
    v = []

    for i in range(n):
        v.append((i, input().index('1')))

    answer = 0

    for i in range(len(v)):
        # We are assuming (0, 0) is the top left corner
        r_left = 0  # The topmost row index within a square (Always 0, just added it for more clarity)
        r_right = 0 # The bottommost row index within a square

        c_left = 0  # The leftmost column within a square (Can be negative)
        c_right = 0 # The rightmost column within a square

        # NOTE: A negative c_left means a column is to the left
        # For example, [(1, 2), (2, 1)] would yield a negative value as (2, 1) is to the left of (1, 2)

        for j in range(i, len(v)):
            if v[j][0] - v[i][0] < r_left: r_left = v[j][0] - v[i][0]
            if v[j][0] - v[i][0] > r_right: r_right = v[j][0] - v[i][0]

            if v[j][1] - v[i][1] < c_left: c_left = v[j][1] - v[i][1]
            if v[j][1] - v[i][1] > c_right: c_right = v[j][1] - v[i][1]

            # For a set of coordinates to be within a square,
            # It's required that differences of any pair <= length of square
            # Here, the differences between the leftmost value and the rightmost values would do the trick
            if abs(r_right - r_left) <= j - i and abs(c_right - c_left) <= j - i:
                answer += 1

    print(answer)