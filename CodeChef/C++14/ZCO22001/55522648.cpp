#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int n, m;
    cin >> n >> m;

    int pre[n][m];
    memset(pre, 0, sizeof pre);

    int g[n][m];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> g[i][j];
            if (g[i][j] == 0)
                pre[i][j]++;
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (i-1 >= 0) pre[i][j] += pre[i-1][j];
            if (j-1 >= 0) pre[i][j] += pre[i][j-1];
            if (i-1 >= 0 && j-1 >= 0) pre[i][j] -= pre[i-1][j-1];
        }
    }

    int q; cin >> q;

    while (q--) {
        int a, b, c, d; cin >> a >> b >> c >> d;
        a--; b--; c--; d--;

        int cnt = pre[c][d];
        if (a-1 >= 0) cnt -= pre[a-1][d];
        if (b-1 >= 0) cnt -= pre[c][b-1];
        if (a-1 >= 0 && b-1 >= 0) cnt += pre[a-1][b-1];

        if (cnt > 0)
            cout << 0 << endl;
        else
            cout << 1 << endl;
    }
}
