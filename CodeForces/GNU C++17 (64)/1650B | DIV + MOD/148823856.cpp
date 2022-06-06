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
        int l, r, a;
        cin >> l >> r >> a;
 
        int v = r - r%a - 1;
 
        if (v >= l)
            cout << max(r / a + r % a, v / a + v % a) << endl;
        else
            cout << r / a + r % a << endl;
    }
}