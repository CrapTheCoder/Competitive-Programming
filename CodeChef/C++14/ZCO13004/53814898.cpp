#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int n, m, k;
    cin >> n >> m >> k;

    bool grid[n][m];
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            grid[i][j] = true;

    for (int c = 0; c < k; c++) {
        int x, y, t, f;
        cin >> x >> y >> t >> f;
        x--; y--;

        grid[x][y] = false;

        for (int i = 0; i < n; i++) {
            int reach = (i+y - t) - abs(i-x);
            if ((reach >= 0) && (reach % f == 0))
                grid[i][y] = false;
        }
        
        for (int j = 0; j < m; j++) {
            int reach = (j+x - t) - abs(j-y);
            if ((reach >= 0) && (reach % f == 0))
                grid[x][j] = false;
        }
    }

    for (int i = 1; i < n; i++) grid[i][0] = grid[i-1][0];
    for (int j = 1; j < m; j++) grid[0][j] = grid[0][j-1];

    for (int i = 1; i < n; i++)
        for (int j = 1; j < m; j++)
            grid[i][j] = (grid[i-1][j] || grid[i][j-1]) && grid[i][j];
    
    if (!grid[n-1][m-1])
        cout << "NO" << endl;

    else {
        cout << "YES" << endl;
        cout << n + m - 2 << endl;
    }
}
