#include <bits/stdc++.h>
using namespace std;

#define endl '\n'
#define int long long

signed main() {
    //ios::sync_with_stdio(false); cin.tie(NULL);

    int n; cin >> n;
    int a[n]; for (int i = 0; i < n; i++) cin >> a[i];
    int b[n]; for (int i = 0; i < n; i++) cin >> b[i];

    int dp[n][n], sp[n][n][2];
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            dp[i][j] = 1, sp[i][j][0] = sp[i][j][1] = -1;

    for (int i = 0; i < n; i++)
        for (int k = 0; k < n; k++)
            for (int j = 0; j < i; j++)
                for (int l = 0; l < k; l++)
                    if ((a[i] - a[j] == b[k] - b[l]) && (dp[j][l] + 1 > dp[i][k]))
                        dp[i][k] = dp[j][l] + 1, sp[i][k][0] = j, sp[i][k][1] = l;

    int maxi = 0;
    int xi = -1, xj = -1;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (dp[i][j] > maxi) {
                maxi = dp[i][j];
                xi = i, xj = j;
            }
        }
    }

    vector<int> ax, bx;

    cout << maxi << endl;
    while (xi != -1 || xj != -1) {
        ax.push_back(a[xi]);
        bx.push_back(b[xj]);
        int nxi = sp[xi][xj][0], nxj = sp[xi][xj][1];
        xi = nxi, xj = nxj;
    }

    reverse(ax.begin(), ax.end());
    reverse(bx.begin(), bx.end());

    for (auto i : ax) cout << i << " ";
    cout << endl;

    for (auto j : bx) cout << j << " ";
    cout << endl;
}
