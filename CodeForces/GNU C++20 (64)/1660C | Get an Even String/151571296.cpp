#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
string s;
int dp[200013][30][2];
 
int solve(int i, char p, int o) {
    if (i == s.size())
        return (o == 1) ? INF : 0;
 
    if (dp[i][p-'a'][o] != -1)
        return dp[i][p-'a'][o];
 
    if (o == 1) {
        if (s[i] == p)
            return dp[i][p-'a'][o] = min(solve(i+1, '{', o^1), solve(i+1, p, o) + 1);
 
        return dp[i][p-'a'][o] = solve(i+1, p, o) + 1;
 
    } else {
        return dp[i][p-'a'][o] = min(solve(i+1, s[i], o^1), solve(i+1, '{', o) + 1);
    }
}
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int tc; cin >> tc;
    while (tc--) {
        cin >> s;
        for (int i = 0; i < s.size() + 5; i++)
            for (int j = 0; j < 30; j++)
                dp[i][j][0] = dp[i][j][1] = -1;
 
        cout << solve(0, '{', 0) << endl;
    }
}