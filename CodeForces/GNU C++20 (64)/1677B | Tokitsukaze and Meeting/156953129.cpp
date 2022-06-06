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
        int n, m; cin >> n >> m;
        string s; cin >> s;
 
        int r[n*m]{}, f = 0;
        for (int i = 0; i < n*m; i++) {
            f += s[i] - '0';
            if (i-m >= 0) {
                f -= s[i-m] - '0';
                r[i] += r[i-m];
            }
 
            if (f)
                r[i]++;
        }
 
        int c[n*m]{}; set<int> g;
        for (int i = 0; i < n*m; i++) {
            if (s[i] == '1')
                g.insert(i % m);
 
            c[i] = g.size();
        }
 
        for (int i = 0; i < n*m; i++)
            cout << r[i] + c[i] << " ";
        cout << endl;
    }
}