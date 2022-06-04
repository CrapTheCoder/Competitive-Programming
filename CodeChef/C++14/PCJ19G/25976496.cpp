#include <bits/stdc++.h>
using namespace std;

int Mid(int s, int e) { return s + (e -s)/2; }

int getSumUtil(int *st, int ss, int se, int l, int r, int si)
{
    if (l <= ss && r >= se)
        return st[si];

    if (se < l || ss > r)
        return 0;

    int mid = Mid(ss, se);
    return getSumUtil(st, ss, mid, l, r, 2*si+1) +
        getSumUtil(st, mid+1, se, l, r, 2*si+2);
}

void updateUtil(int *st, int ss, int se, int i, int diff, int si)
{
    if (i < ss || i > se)
        return;

    st[si] = st[si] + diff;
    
    if (se != ss)
    {
        int mid = Mid(ss, se);
        updateUtil(st, ss, mid, i, diff, 2*si + 1);
        updateUtil(st, mid+1, se, i, diff, 2*si + 2);
    }
}

void update(int arr[], int *st, int n, int i, int x)
{
    int d = x - arr[i];
    arr[i] = x;
    updateUtil(st, 0, n-1, i, d, 0);
}

int getSum(int *st, int n, int l, int r)
{
    return getSumUtil(st, 0, n-1, l, r, 0);
}

int constructUtil(int arr[], int ss, int se, int *st, int si)
{
    if (ss == se)
    {
        st[si] = arr[ss];
        return arr[ss];
    }

    int mid = Mid(ss, se);
    st[si] = constructUtil(arr, ss, mid, st, si*2+1) + constructUtil(arr, mid+1, se, st, si*2+2);

    return st[si];
}

int *construct(int arr[], int n)
{
    int x = (int)(ceil(log2(n)));

    int ms = 2*(int)pow(2, x) - 1;
    int *st = new int[ms];
    constructUtil(arr, 0, n-1, st, 0);

    return st;
}

int main()
{
    int n; cin >> n;
    int arr[n];

    for(int i = 0; i < n; i++)
        cin >> arr[i];

    int *st = construct(arr, n);

    int q; cin >> q;

    for(int i = 0; i < q; i++){
        int x; cin >> x;

        if(x == 1){
            int i, x; cin >> i >> x;
            update(arr, st, n, i-1, x);
        }

        if(x == 2){
            int l, r; cin >> l >> r;
            cout << getSum(st, n, l-1, r-1) << endl;
        }
    }

    return 0;
}
