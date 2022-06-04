#include <bits/stdc++.h>
using namespace std;
 
#define endl '\n'
#define int long long
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int tc; cin >> tc;
    while (tc--) {
        int n, m;
        cin >> n >> m;
 
        int mi = INF, mj = INF;
 
        string a[n];
        for (int i = 0; i < n; i++) {
            cin >> a[i];
            for (int j = 0; j < m; j++)
                if (a[i][j] == 'R')
                    mi = min(mi, i), mj = min(mj, j);
        }
 
        cout << (a[mi][mj] == 'R' ? "YES" : "NO") << endl;
    }
}