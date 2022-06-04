#include <bits/stdc++.h>
using namespace std;
 
#define endl '\n'
#define int long long
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    vector<pair<int, int>> v;
 
    int q; cin >> q;
    while (q--) {
        int t; cin >> t;
        if (t == 1) {
            int x; cin >> x;
            v.push_back({x, -1});
 
        } else {
            int x, y; cin >> x >> y;
            v.push_back({x, y});
        }
    }
 
    reverse(v.begin(), v.end());
 
    vector<int> a;
 
    map<int, int> c;
    for (int i = 0; i <= 5e5 + 13; i++)
        c[i] = i;
 
    for (auto [x, y] : v) {
        if (y == -1)
            a.push_back(c[x]);
        else
            c[x] = c[y];
    }
 
    reverse(a.begin(), a.end());
 
    for (auto i : a)
        cout << i << " ";
    cout << endl;
}