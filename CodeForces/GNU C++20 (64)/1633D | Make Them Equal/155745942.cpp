#include <bits/stdc++.h>
using namespace std;
 
#define int long long
const int INF = LLONG_MAX >> 1;
 
int n, k;
int a[1013], b[1013];
int dp[1013][15000];
int steps[5013];
 
int knapsack(int i = 0, int used = 0) {
    if (used > k)
        return -INF;
 
    if (i == n)
        return 0;
 
    if (dp[i][used] != -1)
        return dp[i][used];
 
    return dp[i][used] = max(knapsack(i+1, used), b[i] + knapsack(i+1, used + steps[a[i]]));
}
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    fill(steps, steps+5013, INF); steps[1] = 0;
    for (int i = 1; i < 2013; i++)
        for (int x = 1; x <= i; x++)
            steps[i + i/x] = min(steps[i + i/x], steps[i] + 1);
 
    int tc; cin >> tc;
    while (tc--) {
        cin >> n >> k;
        for (int i = 0; i < n; i++) cin >> a[i];
        for (int i = 0; i < n; i++) cin >> b[i];
 
        int total = 0, sum = 0;
        for (int i = 0; i < n; i++)
            total += steps[a[i]], sum += b[i];
 
        if (total <= k)
            cout << sum << endl;
 
        else {
            for (int i = 0; i < n+5; i++)
                for (int j = 0; j < k+5; j++)
                    dp[i][j] = -1;
 
            cout << knapsack() << endl;
        }
    }
}