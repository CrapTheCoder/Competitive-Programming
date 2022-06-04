#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'
#define all(iter) (iter).begin(), (iter).end()
#define rall(iter) (iter).rbegin(), (iter).rend()
#define size_of(iter) (int) iter.size();

const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;

int op(int a) {
    int c = 0;
    while (a)
        c += a % 10, a /= 10;
    
    return c*c*c;
}

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int n, s; cin >> n >> s;

    int e[n+1]{}, p[n+1]{}; p[0] = s;
    for (int i = 1; i <= n; i++)
        cin >> e[i], p[i] = p[i-1] + op(p[i-1]);
    
    int dp[n+1][n+1]{};
    for (int i = 1; i <= n; i++)
        for (int j = 0; j < i; j++)
            dp[i][j] = max(dp[i-1][j] + p[j] * e[i], (j-1 >= 0) ? dp[i-1][j-1] : 0);

    int maxi = 0;
    for (int i = 0; i < n; i++)
        maxi = max(maxi, dp[n][i]);
    
    cout << maxi << endl;
}
