#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int t; cin >> t;

    while (t--) {
        int n; cin >> n;

        int a[n];
        for (int i = 0; i < n; i++)
            cin >> a[i];

        int c = 0;
        for (int i = 0; i < n; i++)
            for (int j = i+1; j < n; j++)
                if ((a[i] ^ a[j]) > max(a[i], a[j]))
                    c++;

        cout << c << endl;
    }
}
