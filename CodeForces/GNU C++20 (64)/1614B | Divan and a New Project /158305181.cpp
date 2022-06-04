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
 
        int res[n+1]{}; pair<int, int> a[n];
        for (int i = 0; i < n; i++)
            cin >> a[i].first, a[i].second = i;
 
        sort(a, a+n, greater<pair<int, int>>());
 
        int cur = 1, s = 0;
        for (int i = 0; i < n; i++) {
            res[a[i].second + 1] = cur;
            s += 2 * abs(cur) * a[i].first;
            cur = -cur + i%2;
        }
 
        cout << s << endl;
        for (auto i : res)
            cout << i << " ";
        cout << endl;
    }
}