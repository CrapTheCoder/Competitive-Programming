#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'
#define all(iter) (iter).begin(), (iter).end()
#define rall(iter) (iter).rbegin(), (iter).rend()

const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;

int n, k;
int v[713], b[713];
int dp[713][713];
bool vis[713][713];

int solve(int l, int r) {
    if (l >= r)
        return 0;

    if (vis[l][r])
        return dp[l][r];

    int maxi = -INF;
    for (int i = l; i <= r-1; i++)
        maxi = max(maxi, solve(l, i) + solve(i+1, r));
    
    if (b[l] + k == b[r])
        maxi = max(maxi, solve(l+1, r-1) + v[l] + v[r]);
    
    vis[l][r] = true;
    return dp[l][r] = maxi;
}

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    memset(vis, false, sizeof vis);

    cin >> n >> k;
    for (int i = 0; i < n; i++) cin >> v[i];
    for (int i = 0; i < n; i++) cin >> b[i];

    cout << solve(0, n-1) << endl;
}
