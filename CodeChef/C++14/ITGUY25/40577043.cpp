#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int t; cin >> t;

    while (t--) {
        int n; cin >> n;
        int c = 0;

        while (n) {
            if (n & 1)
                c++;

            n >>= 1;
        }

        cout << c << endl;
    }
}
