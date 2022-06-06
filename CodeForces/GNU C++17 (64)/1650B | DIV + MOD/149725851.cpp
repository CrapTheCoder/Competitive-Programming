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
 
        int val = (r / a) * a - 1;
 
        if (val < l) {
            cout << (r / a) + (r % a) << endl;
 
        } else {
            cout << max((val / a) + (val % a), (r / a) + (r % a)) << endl;
        }
    }
}