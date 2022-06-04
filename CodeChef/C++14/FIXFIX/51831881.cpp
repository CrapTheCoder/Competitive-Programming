#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int tc; cin >> tc;

    while (tc--) {
        int n, k; cin >> n >> k;

        if (n == k){
            for (int i = 0; i < n; i++)
                cout << i+1 << " ";
            cout << endl;
            continue;
        }

        int a[n];
        for (int i = 0; i < k; i++)
            a[i] = i+1;

        a[k] = n;
        for (int i = k+1; i < n; i++)
            a[i] = i;

        int c = 0;
        for (int i = 0; i < n; i++)
            if (a[i] == i+1)
                c++;

        if (c != k) {
            cout << -1 << endl;
            continue;
        }

        for (int i = 0; i < n; i++)
            cout << a[i] << " ";
        cout << endl;
    }
}
