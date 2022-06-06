#include <bits/stdc++.h>
 
using namespace std;
 
#define endl '\n'
#define int long long
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int n, m; cin >> n >> m;
 
    int a[26]{};
    for (int i = 0; i < n; i++) {
        char c; cin >> c;
        a[c - 'A']++;
    }
 
    sort(a, a + 26, greater<int>());
 
    int ans = 0;
    for (int i = 0; i < 26; i++) {
        int d = min(m, a[i]);
        ans += d * d;
        m -= d;
    }
 
    cout << ans << endl;
}