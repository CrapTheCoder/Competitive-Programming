# https://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/
from math import ceil, log2;


# A utility function to get the
# middle index from corner indexes.
def getMid(s, e):
    return s + (e - s) // 2;


""" A recursive function to get the sum of values
    in the given range of the array. The following
    are parameters for this function.

    st --> Pointer to segment tree
    si --> Index of current node in the segment tree.
           Initially 0 is passed as root is always at index 0
    ss & se --> Starting and ending indexes of the segment
                represented by current node, i.e., st[si]
    qs & qe --> Starting and ending indexes of query range """


def getSumUtil(st, ss, se, qs, qe, si):
    # If segment of this node is a part of given range,
    # then return the sum of the segment
    if (qs <= ss and qe >= se):
        return st[si];

        # If segment of this node is
    # outside the given range
    if (se < qs or ss > qe):
        return 0;

        # If a part of this segment overlaps
    # with the given range
    mid = getMid(ss, se);

    return getSumUtil(st, ss, mid, qs, qe, 2 * si + 1) + \
           getSumUtil(st, mid + 1, se, qs, qe, 2 * si + 2);


""" A recursive function to update the nodes
which have the given index in their range.
The following are parameters st, si, ss and se
are same as getSumUtil()
i --> index of the element to be updated.
      This index is in the input array.
diff --> Value to be added to all nodes
which have i in range """


def updateValueUtil(st, ss, se, i, diff, si):
    # Base Case: If the input index lies
    # outside the range of this segment
    if (i < ss or i > se):
        return;

        # If the input index is in range of this node,
    # then update the value of the node and its children
    st[si] = st[si] + diff;

    if (se != ss):
        mid = getMid(ss, se);
        updateValueUtil(st, ss, mid, i,
                        diff, 2 * si + 1);
        updateValueUtil(st, mid + 1, se, i,
                        diff, 2 * si + 2);

    # The function to update a value in input array


# and segment tree. It uses updateValueUtil()
# to update the value in segment tree
def updateValue(arr, st, n, i, new_val):
    # Check for erroneous input index
    if (i < 0 or i > n - 1):
        print("Invalid Input", end="");
        return;

        # Get the difference between
    # new value and old value
    diff = new_val - arr[i];

    # Update the value in array
    arr[i] = new_val;

    # Update the values of nodes in segment tree
    updateValueUtil(st, 0, n - 1, i, diff, 0);


# Return sum of elements in range from
# index qs (quey start) to qe (query end).
# It mainly uses getSumUtil()
def getSum(st, n, qs, qe):
    # Check for erroneous input values
    if (qs < 0 or qe > n - 1 or qs > qe):
        print("Invalid Input", end="");
        return -1;

    return getSumUtil(st, 0, n - 1, qs, qe, 0);


# A recursive function that constructs
# Segment Tree for array[ss..se].
# si is index of current node in segment tree st
def constructSTUtil(arr, ss, se, st, si):
    # If there is one element in array,
    # store it in current node of
    # segment tree and return
    if (ss == se):
        st[si] = arr[ss];
        return arr[ss];

        # If there are more than one elements,
    # then recur for left and right subtrees
    # and store the sum of values in this node
    mid = getMid(ss, se);

    st[si] = constructSTUtil(arr, ss, mid, st, si * 2 + 1) + \
             constructSTUtil(arr, mid + 1, se, st, si * 2 + 2);

    return st[si];


""" Function to construct segment tree
from given array. This function allocates memory
for segment tree and calls constructSTUtil() to
fill the allocated memory """


def constructST(arr, n):
    # Allocate memory for the segment tree

    # Height of segment tree
    x = (int)(ceil(log2(n)));

    # Maximum size of segment tree
    max_size = 2 * (int)(2 ** x) - 1;

    # Allocate memory
    st = [0] * max_size;

    # Fill the allocated memory st
    constructSTUtil(arr, 0, n - 1, st, 0);

    # Return the constructed segment tree
    return st;

def main():
    n = int(input())
    m = list(map(int, input().split()))

    q = int(input())

    st = constructST(m, n)

    for _ in range(q):
        a, b, c = map(int, input().split())

        if a == 0:
            b -= 1
            updateValue(m, st, n, b, m[b] + c)

        else:
            b -= 1
            c -= 1

            if c < b:
                print(0)
                continue

            s = getSum(st, n, b, c)

            print(-(-s // (c - b + 1)))

main()