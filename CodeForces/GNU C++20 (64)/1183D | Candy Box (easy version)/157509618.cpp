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
        int n; cin >> n;
        int a[n+1]{};
        for (int i = 0; i < n; i++) {
            int x; cin >> x; a[x]++;
        }
 
        sort(a+1, a+n+1);
 
        int cur = INF, ans = 0;
        for (int i = n; i > 0; i--) {
            cur = min(cur-1, a[i]);
            if (cur > 0) ans += cur;
        }
 
        cout << ans << endl;
    }
}