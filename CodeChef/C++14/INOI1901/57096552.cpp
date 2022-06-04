#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'
#define all(iter) (iter).begin(), (iter).end()
#define rall(iter) (iter).rbegin(), (iter).rend()

const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int tc; cin >> tc;
    while (tc--) {
        int n, m;
        cin >> n >> m;

        int q[n+1], p[m+1], t[m+1];
        pair<int, int> tp[m+1];
        for (int i = 1; i <= n; i++) cin >> q[i];
        for (int i = 1; i <= m; i++) cin >> tp[i].second;
        for (int i = 1; i <= m; i++) cin >> tp[i].first;

        sort(tp+1, tp+m+1);

        for (int i = 1; i <= m; i++)
            p[i] = tp[i].second, t[i] = tp[i].first;

        int dp[n+1][m+1]{};

        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= m; j++) {
                if (i == 0 && j == 0)
                    continue;

                int a1 = INF;
                if ((j-1 >= 0) && (dp[i][j-1] <= t[j]))
                    a1 = max(dp[i][j-1] + p[j], t[j]);

                int a2 = INF;
                if (i-1 >= 0)
                    a2 = dp[i-1][j] + q[i];
                
                dp[i][j] = min(a1, a2);
            }
        }

        cout << (dp[n][m] == INF ? -1 : dp[n][m]) << endl;
    }
}
