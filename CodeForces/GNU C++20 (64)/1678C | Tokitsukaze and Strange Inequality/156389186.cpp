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
 
        int r[n+1];
        for (int i = 1; i <= n; i++)
            cin >> r[i];
 
        int ans = 0;
 
        for (int b = 1; b <= n; b++) {
            int p[n+1]{};
            for (int a = 1; a < b; a++) p[r[a]]++;
            for (int i = 1; i <= n; i++) p[i] += p[i-1];
 
            int f = 0;
            for (int c = n; c > b; c--) {
                ans += f * p[r[c]];
                f += r[c] < r[b];
            }
        }
 
        cout << ans << endl;
    }
}