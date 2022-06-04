#include <vector>
#include <bits/stdc++.h>
using namespace std;

int bs(int a[], int l, int r, int key)
{
    while(r - l > 1){
        int m = l + (r - l) / 2;

        if (a[m] >= key)
            r = m;
        else
            l = m;
    }

    return r;
}

int LIS(int a[], int n)
{
    int l = 1;
    int t[n]; memset(t, 0, sizeof t);
    t[0] = a[0];

    for(int i = 1; i < n; i++){
        if(a[i] < t[0]) t[0] = a[i];
        else if(a[i] > t[l - 1]) t[l++] = a[i];
        else t[bs(t, -1, l - 1, a[i])] = a[i];
	}

    return l;
}

int main()
{
    int t; cin >> t;

    while(t--){
        int n; cin >> n;
        int a[n];

        for(int i = 0; i < n; i++)
            cin >> a[i];

        cout << LIS(a, n) << endl;
    }

    return 0;
}
