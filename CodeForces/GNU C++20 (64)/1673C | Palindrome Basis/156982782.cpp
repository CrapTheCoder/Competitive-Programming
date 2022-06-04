#include <bits/stdc++.h>
using namespace std;
 
#define endl '\n'
#define int long long
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
vector<int> pals;
int dp[40013];
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    for (int i = 1; i <= 4e4 + 13; i++) {
        string si = to_string(i);
        string rev = si; ranges::reverse(rev);
 
        if (si == rev)
            pals.push_back(i);
    }
 
    dp[0] = 1;
    for (int j : pals)
        for (int i = 1; i <= 4e4; i++)
            if (i - j >= 0)
                dp[i] = (dp[i] + dp[i-j]) % MOD;
 
    int tc; cin >> tc;
    while (tc--) {
        int n; cin >> n;
        cout << dp[n] << endl;
    }
}