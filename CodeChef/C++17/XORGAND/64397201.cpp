#include <bits/stdc++.h>
using namespace std;

#define endl '\n'
#define int long long

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int tc; cin >> tc;
    while (tc--) {
        int n; cin >> n;
        int pre[n+1][35]{};

        for (int i = 1; i <= n; i++) {
            int x; cin >> x;

            int c = 0;
            while (x)
                c++, x >>= 1;

            pre[i][c]++;
            for (int j = 0; j < 35; j++)
                pre[i][j] += pre[i-1][j];
        }

        int q; cin >> q;
        while (q--) {
            int l, r, x; cin >> l >> r >> x;

            int c = 0;
            while (x)
                c++, x >>= 1;

            cout << (r - l + 1) - (pre[r][c] - pre[l-1][c]) << endl;
        }
    }
}