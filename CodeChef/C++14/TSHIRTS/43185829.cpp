#include <bits/stdc++.h>
using namespace std;

#define endl '\n'
#define int long long
#define INF LLONG_MAX >> 1
#define MOD 1000000007

int n, all;
int dp[1 << 13][113];
vector<int> ta[113];

int solve(int m=0, int c=1) {
    if (m == all)
        return 1;

    if (c > 100)
        return 0;

    if (dp[m][c] != -1)
        return dp[m][c];

    int t = solve(m, c+1);

    for (auto i : ta[c])
        if (!(m & (1 << i)))
            t = (t + solve(m | (1 << i), c+1)) % MOD;

    return dp[m][c] = t;
}

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int tcs; cin >> tcs;
    while (tcs--) {
        for (int i = 0; i < 113; i++)
            ta[i].clear();

        for (int i = 0; i < 1 << 13; i++)
            for (int j = 0; j < 113; j++)
                dp[i][j] = -1;

        cin >> n;
        cin.ignore();

        for (int i = 0; i < n; i++) {
            string line;

            getline(cin, line);
            stringstream s(line);

            int curi;
            while (s >> curi)
                ta[curi].push_back(i);
        }

        all = (1 << n) - 1;
        cout << solve() << endl;
    }
}
