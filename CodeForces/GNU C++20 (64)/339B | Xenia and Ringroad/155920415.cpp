#include <bits/stdc++.h>
using namespace std;
 
#define endl '\n'
#define int long long
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int n, m;
    cin >> n >> m;
 
    int cur = 0, t = 0;
    for (int i = 0; i < m; i++) {
        int x; cin >> x; x--;
        t += (x - cur + n) % n;
        cur = x;
    }
 
    cout << t << endl;
}