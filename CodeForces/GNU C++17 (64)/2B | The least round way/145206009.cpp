#include <bits/stdc++.h>
using namespace std;
 
#define endl '\n'
const int INF = INT_MAX >> 1;
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int n; cin >> n;
 
    pair<int, int> grid[n][n];
    bool has0 = false;
    int i0, j0;
 
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int x; cin >> x;
 
            if (x == 0) {
                grid[i][j] = {INF, INF};
                has0 = true, i0 = i, j0 = j;
                continue;
            }
 
            while (x % 2 == 0) x /= 2, grid[i][j].first++;
            while (x % 5 == 0) x /= 5, grid[i][j].second++;
        }
    }
 
    pair<pair<int, int>, char> dp1[n][n], dp2[n][n];
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            dp1[i][j] = dp2[i][j] = {{INF, INF}, 'X'};
 
    dp1[0][0] = {{0, 0}, '~'};
    dp2[0][0] = {{0, 0}, '~'};
 
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i-1 >= 0) dp1[i][j] = min(dp1[i][j], dp1[i-1][j]), dp2[i][j] = min(dp2[i][j], dp2[i-1][j]);
            if (j-1 >= 0) dp1[i][j] = min(dp1[i][j], dp1[i][j-1]), dp2[i][j] = min(dp2[i][j], dp2[i][j-1]);
 
            if (i-1 >= 0) {
                if (dp1[i][j] == dp1[i-1][j]) dp1[i][j].second = 'D';
                if (dp2[i][j] == dp2[i-1][j]) dp2[i][j].second = 'D';
            }
 
            if (j-1 >= 0) {
                if (dp1[i][j] == dp1[i][j-1]) dp1[i][j].second = 'R';
                if (dp2[i][j] == dp2[i][j-1]) dp2[i][j].second = 'R';
            }
 
            dp1[i][j].first.first += grid[i][j].first, dp1[i][j].first.second += grid[i][j].second;
            dp2[i][j].first.first += grid[i][j].second, dp2[i][j].first.second += grid[i][j].first;
        }
    }
 
//    for (int i = 0; i < n; i++) {
//        for (int j = 0; j < n; j++)
//            cout << "(" << dp1[i][j].first.first << ", " << dp1[i][j].first.second << ", " << dp2[i][j].second << ") ";
//        cout << endl;
//    }
//
//    cout << endl;
//
//    for (int i = 0; i < n; i++) {
//        for (int j = 0; j < n; j++)
//            cout << "(" << dp2[i][j].first.first << ", " << dp2[i][j].first.second << ", " << dp2[i][j].second << ") ";
//        cout << endl;
//    }
 
    int m1 = min(dp1[n-1][n-1].first.first, dp1[n-1][n-1].first.second);
    int m2 = min(dp2[n-1][n-1].first.first, dp2[n-1][n-1].first.second);
 
    if (has0 && min(m1, m2) > 1) {
        cout << 1 << endl;
 
        int i = 0, j = 0;
 
        while (i != i0) cout << "D", i++;
        while (j != j0) cout << "R", j++;
        while (i != n-1) cout << "D", i++;
        while (j != n-1) cout << "R", j++;
        cout << endl;
 
        return 0;
    }
 
    string res;
 
    if (m1 < m2) {
        for (int i = n-1, j = n-1; i != 0 || j != 0;) {
            res += dp1[i][j].second;
            int ni = i, nj = j;
            if (dp1[ni][nj].second == 'D') i--;
            if (dp1[ni][nj].second == 'R') j--;
        }
 
        cout << m1 << endl;
 
    } else {
        for (int i = n-1, j = n-1; i != 0 || j != 0;) {
            res += dp2[i][j].second;
            int ni = i, nj = j;
            if (dp2[ni][nj].second == 'D') i--;
            if (dp2[ni][nj].second == 'R') j--;
        }
 
        cout << m2 << endl;
    }
 
    reverse(res.begin(), res.end());
    cout << res << endl;
}