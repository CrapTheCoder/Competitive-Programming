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
        int n, q; cin >> n >> q;
        int a[n];
        for (int i = 0; i < n; i++)
            cin >> a[i];
 
        int ans = 0;
        bool t = false;
 
        for (int i = 0; i < n; i++) {
            if (!t) {
                if (i+1 == n || a[i] > a[i+1])
                    ans += a[i], t = !t;
 
            } else {
                if (i+1 < n && a[i] < a[i+1])
                    ans -= a[i], t = !t;
            }
        }
 
        cout << ans << endl;
    }
}