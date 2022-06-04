#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;

const vector<pair<int, int>> dir = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int tc; cin >> tc;
    while (tc--) {
        int n, m; cin >> n >> m;
        int a, b; cin >> a >> b;
        int c, d; cin >> c >> d;

        int grid[n+1][m+1]{};
        grid[a][b] = 1;
        grid[c][d] = 2;

        int cur = 1;
        if ((a + b) % 2)
            cur = 2;

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (grid[i][j] == 0)
                    grid[i][j] = cur;

                cur = (cur == 1) ? 2 : 1;
            }

            if (!(m % 2))
                cur = (cur == 1) ? 2 : 1;
        }

        for (auto [x, y] : dir) {
            int i = c + x, j = d + y;
            if ((1 <= i && i <= n) && (1 <= j && j <= m))
                if (grid[i][j] == grid[c][d])
                    grid[i][j] = 3;
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++)
                cout << grid[i][j] << " ";
            cout << endl;
        }
    }
}
