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
 
        set<int> a;
        for (int i = 0; i < n; i++) {
            int x; cin >> x;
            a.insert(x);
        }
 
        for (int k = 1; k <= n; k++)
            cout << max((int)a.size(), k) << " ";
        cout << endl;
    }
}