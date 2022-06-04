#include <bits/stdc++.h>
using namespace std;

#define endl '\n'
#define MOD 100000007

int n, m, k;

int dp[113][113][213][2];
int a[113];
int b[113];

int solve(int i=0, int j=0, int x=0, int l=-1) {
    if (i == n && j == m) {
        if (x == k)
            return 1;
        else
            return 0;
    }

    if (l != -1)
        if (dp[i][j][x][l] != -1)
            return dp[i][j][x][l];

    int c = 0;

    if (i < n) {
        int cb = x + 1;

        if (l == 0 and a[i] == a[i-1]) cb--;
        if (l == 1 and a[i] == b[j-1]) cb--;

        c += solve(i+1, j, cb, 0);
        c %= MOD;
    }

    if (j < m) {
        int cb = x + 1;

        if (l == 0 and b[j] == a[i-1]) cb--;
        if (l == 1 and b[j] == b[j-1]) cb--;

        c += solve(i, j+1, cb, 1);
        c %= MOD;
    }

    return dp[i][j][x][l] = c;
}

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int t; cin >> t;

    while (t--) {
        cin >> n >> m >> k;

        for (int i = 0; i < n; i++) cin >> a[i];
        for (int i = 0; i < m; i++) cin >> b[i];

        for (int i = 0; i < 113; i++)
            for (int j = 0; j < 113; j++)
                for (int x = 0; x < 213; x++)
                    dp[i][j][x][0] = dp[i][j][x][1] = -1;

        cout << solve() << endl;
    }
}
