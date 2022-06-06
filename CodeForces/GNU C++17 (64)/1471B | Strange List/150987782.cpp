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
        int n, x; cin >> n >> x;
        queue<pair<int, int>> a;
        for (int i = 0; i < n; i++) {
            int r; cin >> r;
            a.push({r, 1});
        }
 
        int sum = 0;
        while (!a.empty()) {
            auto [i, c] = a.front();
            if (i % x != 0)
                break;
 
            a.pop();
            sum += i * c;
            a.push({i/x, c*x});
        }
 
        while (!a.empty()) {
            auto [i, c] = a.front(); a.pop();
            sum += i*c;
        }
 
        cout << sum << endl;
    }
}