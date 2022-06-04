#include <bits/stdc++.h>
using namespace std;
 
#define endl '\n'
#define int long long
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
int n, k;
int b[1013], c[1013], cost[4013];
int dp[1013][15013];
 
int solve(int i, int r) {
    if (r < 0) return -INF;
    if (i == n) return 0;
 
    if (dp[i][r] != -1)
        return dp[i][r];
 
    return dp[i][r] = max(solve(i+1, r - cost[b[i]]) + c[i], solve(i+1, r));
}
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    fill(cost, cost+4013, INF); cost[1] = 0;
    for (int i = 1; i < 2000; i++)
        for (int x = 1; x <= i; x++)
            cost[i + i/x] = min(cost[i] + 1, cost[i + i/x]);
 
    int tc; cin >> tc;
    while (tc--) {
        cin >> n >> k;
        memset(dp, -1, sizeof dp);
 
        for (int i = 0; i < n; i++) cin >> b[i];
        for (int i = 0; i < n; i++) cin >> c[i];
 
        int s = accumulate(c, c+n, 0);
 
        if (n*15 <= k) {
            cout << s << endl;
            continue;
        }
 
        cout << solve(0, k) << endl;
    }
}