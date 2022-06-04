#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int t; cin >> t;

    while (t--) {
        int n; cin >> n;

        int c = 1;
        int s = 0;
        while (n) {
            if (n & 1) {
                s += c;
            }

            n >>= 1;
            c *= 6;
        }

        cout << s << endl;
    }
}
