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
        int x, y, k;
        cin >> x >> y >> k;
 
        int cs = k*y + k - 1;
        int ds = x-1;
 
        cout << (cs + ds - 1) / ds + k << endl;
    }
}