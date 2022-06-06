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
        int a[n]; double s = 0;
        for (int i = 0; i < n; i++)
            cin >> a[i], s += a[i];
 
        s /= n;
 
        int ans = 0;
        map<double, int> p;
 
        for (auto i : a)
            ans += p[2*s - i], p[i]++;
 
        cout << ans << endl;
    }
}
 