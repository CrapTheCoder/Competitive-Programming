#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int tc; cin >> tc;
    while (tc--) {
        int n; cin >> n;
 
        if (n == 2) {
            cout << "-1" << endl;
            continue;
        }
 
        int x = 1;
        int ans[n][n];
 
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if ((i + j) % 2 == 0)
                    ans[i][j] = x++;
 
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if ((i + j) % 2 == 1)
                    ans[i][j] = x++;
 
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++)
                cout << ans[i][j] << " ";
            cout << endl;
        }
    }
}