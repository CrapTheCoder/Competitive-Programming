#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'
#define all(iter) (iter).begin(), (iter).end()
#define rall(iter) (iter).rbegin(), (iter).rend()
#define size_of(iter) (int) iter.size();

const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;

int n;
int a[1000013];
int dp[1000013][2];

int calc(int i, int s) {
    if (i == n-1)
        return dp[i][s] = 1;

    if (dp[i][s] != -1)
        return dp[i][s];
    
    if (s == 0 && a[i] <= a[i+1]) return dp[i][s] = calc(i+1, s^1) + 1;
    if (s == 1 && a[i] >= a[i+1]) return dp[i][s] = calc(i+1, s^1) + 1;
    
    return dp[i][s] = 1;
}

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int tc; cin >> tc;
    while (tc--) {
        cin >> n;
        for (int i = 0; i < n; i++) {
            cin >> a[i];
            dp[i][0] = dp[i][1] = -1;
        }

        for (int i = 0; i < n; i++) {
            calc(i, 0); calc(i, 1);
        }

        int maxi = 0;
        for (int i = 0; i < n; i++) {
            if (i + dp[i][0] == n) {
                maxi = max(maxi, dp[i][0] + 1);
                continue;
            }

            if (dp[i][0] % 2 == 0) maxi = max(maxi, dp[i][0] + 1 + dp[i + dp[i][0]][1]);
            if (dp[i][0] % 2 == 1) maxi = max(maxi, dp[i][0] + 1 + dp[i + dp[i][0]][0]);
        }

        cout << maxi << endl;
    }
}
