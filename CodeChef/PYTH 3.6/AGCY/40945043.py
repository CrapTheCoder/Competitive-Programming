from collections import defaultdict

for _ in range(int(input())):
    n, q = map(int, input().split())

    # defaultdict(list) assigns the value as an empty list for each key by default
    # ind stores a unique value for each range
    ind = defaultdict(list)

    # Unique value for each range
    unique_val = 1

    for _ in range(q):
        l, r = map(int, input().split())

        # Converting to 0-based indexing
        l -= 1
        r -= 1

        # Positive denotes beginning
        ind[l].append(unique_val)

        # Negative denotes ending
        # We use r+1 because r is inclusive in the range
        ind[r+1].append(-unique_val)

        # Next value to make it unique
        unique_val += 1

    no_sts = 0  # Number of statues that will be destroyed
    ispeed = 0  # Speed at which the number of statues destroyed increases

    # First occurrence of a range (stores l value of a range)
    occ = {}

    for i in range(n):
        # For each "endpoint" (which is l or r+1)
        for j in ind[i]:

            # If it's a new range the speed with which the number of statues is destroyed will increase
            if j > 0:
                occ[j] = i
                ispeed += 1

            # If it's the end of a range
            # The speed with which the number of statues is destroyed will decrease

            # The current amount of statues which are being destroyed at each index will decrease by how much it has contributed
            # Which is equal to r - l + 1, but since we set the endpoint to r+1, we should make it r - l
            # Here, (r = i) and (l = [first occurrence of -j] = occ[-j])
            elif j < 0:
                ispeed -= 1
                no_sts -= i - occ[-j]

        # The amount of statues destroyed at each index increases by the speed
        no_sts += ispeed

        print(no_sts, end=' ')

    print()
