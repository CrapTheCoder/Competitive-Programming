#include <bits/stdc++.h>
using namespace std;

#define endl '\n'
#define int long long

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int t; cin >> t;

    while (t--) {
        int n, m, k;
        cin >> n >> m >> k;

        char a[n][m];
        int pre[n][m];

        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                pre[i][j] = 0;

        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                cin >> a[i][j];

        int c0 = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                pre[i][j] = 0;
                if (i > 0) pre[i][j] += pre[i-1][j];
                if (j > 0) pre[i][j] += pre[i][j-1];
                if (i > 0 && j > 0) pre[i][j] -= pre[i-1][j-1];

                if (a[i][j] == '0') {
                    c0++;
                    pre[i][j]++;
                }
            }
        }

        if (c0 == 0) {
            cout << 0 << endl;
            continue;
        }

        int maxi = 1;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                int l = 0, r = min(i, j);
                while (l < r) {
                    int m = (l+r+1) / 2;
                    int i1 = i-m, j1 = j-m;

                    if ((m+1)*(m+1) > c0) {
                        r = m-1;
                        continue;
                    }

                    int c = pre[i][j];
                    if (i1 > 0) c -= pre[i1-1][j];
                    if (j1 > 0) c -= pre[i][j1-1];
                    if (i1 > 0 && j1 > 0) c += pre[i1-1][j1-1];

                    if ((m+1)*(m+1) - c > k)
                        r = m-1;
                    else
                        l = m;
                }

                maxi = max(maxi, l+1);
            }
        }

        cout << maxi << endl;
    }
}
