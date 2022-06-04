#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

const int INF = LLONG_MAX >> 1;

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int tc; cin >> tc;
    while (tc--){
        int n, m, k; cin >> n >> m >> k;
        int p[n+1][m+1], dp1[n+1][m+1][k+1], dp2[n+1][m+1][k+1];
        memset(p, 0, sizeof p);
        memset(dp1, 0, sizeof dp1);
        memset(dp2, 0, sizeof dp2);

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                cin >> p[i][j]; p[i][j] += p[i][j-1];
            }
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                dp1[i][j][0] = dp1[i-1][j][0] + p[i][j];
                dp2[i][j][0] = dp2[i-1][j][0] + p[i][j];
                for (int l = 1; l <= k; l++) {
                    dp1[i][j][l] = max(dp1[i-1][j-1][l-1], dp1[i-1][j][l]) + p[i][j];
                    dp2[i][j][l] = min(dp2[i-1][j-1][l-1], dp2[i-1][j][l]) + p[i][j];
                }
            }
        }

        int maxi = -INF;
        for (int i = 1; i <= m; i++)
            for (int j = i+k+1; j <= m; j++)
                maxi = max(maxi, dp1[n][j][k] - dp2[n][i-1][k]);
            
        cout << maxi << endl;
    }
}