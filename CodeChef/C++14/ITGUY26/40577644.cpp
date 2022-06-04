#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int a[] = { 1,
                1,
                2,
                6,
                24,
                120,
                720,
                5040,
                40320,
                362880,
                3628800,
                39916800
            };


    int t; cin >> t;

    while (t--) {
        int n; cin >> n;

        if (n == 0) {
            cout << 0 << endl;
            continue;
        }

        int on = n;
        int s = 0;

        while (n) {
            s += a[n % 10];
            n /= 10;
        }

        if (s == on) cout << 1 << endl;
        if (s != on) cout << 0 << endl;
    }
}
