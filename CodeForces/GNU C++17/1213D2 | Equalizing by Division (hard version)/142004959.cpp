#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
#define all(iter) (iter).begin(), (iter).end()
#define rall(iter) (iter).rbegin(), (iter).rend()
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int n, k; cin >> n >> k;
    map<int, vector<int>> m;
 
    for (int i = 0; i < n; i++) {
        int x; cin >> x;
        int c = 0;
 
        while (x) {
            m[x].push_back(c);
            x /= 2; c++;
        }
    }
 
    int mini = INF;
    for (auto [x, y] : m) {
        if (y.size() >= k) {
            sort(all(y)); int cur = 0;
            for (int i = 0; i < k; i++)
                cur += y[i];
 
            mini = min(mini, cur);
        }
    }
 
    cout << mini << endl;
}