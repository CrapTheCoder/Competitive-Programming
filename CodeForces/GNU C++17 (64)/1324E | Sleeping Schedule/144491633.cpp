#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
int n, h, l, r;
int a[2013];
int dp[2013][2013];
 
int solve(int i = 0, int time = 0) {
    if (i == n)
        return 0;
    
    if (dp[i][time] != -1)
        return dp[i][time];
 
    int s1 = (time + a[i]) % h;
    int s2 = (time + a[i] - 1) % h;
 
    return dp[i][time] = max(solve(i+1, s1) + (l <= s1 && s1 <= r), solve(i+1, s2) + (l <= s2 && s2 <= r));
}
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    cin >> n >> h >> l >> r;    
    for (int i = 0; i < n; i++)
        cin >> a[i];
    
    memset(dp, -1, sizeof dp);
    
    cout << solve() << endl;
}