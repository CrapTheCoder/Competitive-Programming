#include <bits/stdc++.h>
using namespace std;
 
#define endl '\n'
#define int long long
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int n, m, q;
    cin >> n >> m >> q;
 
    vector<int> a(n*m);
    for (int x = 0; x < n; x++) {
        for (int y = 0; y < m; y++) {
            char c; cin >> c;
            a[x + y*n] = (c == '*');
        }
    }
 
    int t = accumulate(a.begin(), a.end(), 0);
    int c = accumulate(a.begin() + t, a.end(), 0);
 
    while (q--) {
        int x, y; cin >> x >> y;
        x--; y--;
 
        int k = x + y*n;
        a[k] ^= 1;
 
        if (k < t) (a[k] == 1) ? c-- : c++;
        if (a[k] == 1 && a[t++] == 0) c++;
        if (a[k] == 0 && a[--t] == 0) c--;
        
        cout << c << endl;
    }
}