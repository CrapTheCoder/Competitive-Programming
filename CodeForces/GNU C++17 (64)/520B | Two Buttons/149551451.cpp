#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int n, m;
    cin >> n >> m;
 
    queue<pair<int, int>> q;
    q.push({n, 0});
 
    set<int> vis;
 
    while (true) {
        auto [cur, cur_dep] = q.front(); q.pop();
 
        if (vis.count(cur)) continue;
        vis.insert(cur);
 
        if (cur == m) {
            cout << cur_dep << endl;
            break;
        }
 
        if (cur-1 > 0)
            q.push({cur-1, cur_dep + 1});
 
        if (cur*2 < 10013)
            q.push({cur*2, cur_dep + 1});
    }
}