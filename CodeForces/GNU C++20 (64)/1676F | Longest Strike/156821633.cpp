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
        int n, k;
        cin >> n >> k;
 
        map<int, int> d;
        for (int i = 0; i < n; i++) {
            int x; cin >> x;
            d[x]++;
        }
 
        set<int> s;
        for (auto [x, y] : d)
            if (y >= k)
                s.insert(x);
 
        if (s.empty()) {
            cout << -1 << endl;
            continue;
        }
 
        pair<int, int> maxi = {-1, -2}, cur;
 
        int p = -1;
        for (auto i : s) {
            if (i == p+1)
                cur.second = i;
            else
                cur = {i, i};
 
            if (cur.second - cur.first > maxi.second - maxi.first)
                maxi = cur;
 
            p = i;
        }
 
        cout << maxi.first << " " << maxi.second << endl;
    }
}