#include <bits/stdc++.h>
using namespace std;
 
#define endl '\n'
#define int long long
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
int n, m;
 
bool check(vector<vector<int>> &a) {
    for (int i = 0; i < n; i++)
        for (int j = 1; j < m; j++)
            if (a[i][j-1] > a[i][j])
                return false;
 
    return true;
}
 
void cswap(vector<vector<int>> &a, int i, int j) {
    for (int k = 0; k < n; k++)
        swap(a[k][i], a[k][j]);
}
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int tc; cin >> tc;
    while (tc--) {
        cin >> n >> m;
 
        vector<vector<int>> a(n, vector<int>(m));
 
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                cin >> a[i][j];
 
        bool f[m]{};
 
        for (int i = 0; i < n; i++) {
            vector<int> b = a[i];
            ranges::sort(b);
 
            for (int j = 0; j < m; j++)
                if (a[i][j] != b[j])
                    f[j] = true;
        }
 
        vector<int> ind;
        for (int i = 0; i < m; i++)
            if (f[i])
                ind.push_back(i);
 
        if (ind.size() == 0) {
            cout << 1 << " " << 1 << endl;
            continue;
        }
 
        if (ind.size() == 2) {
            cswap(a, ind[0], ind[1]);
            if (check(a)) {
                cout << ind[0] + 1 << " " << ind[1] + 1 << endl;
                continue;
            }
        }
 
        cout << -1 << endl;
    }
}