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
 
    int x = 0, end = 0;
 
    int ans = 0;
    for (int c = 0; c < n; c++) {
        string s; cin >> s;
 
        int f = -1, l = -1;
 
        for (int i = 0; i < m; i++) {
            if (s[i] == 'W') {
                l = i;
                if (f == -1)
                    f = i;
            }
        }
 
        if (c != 0)
            ans++;
 
        if (f == -1 || l == -1) {
            end++;
 
        } else {
            end = 0;
 
            if (c % 2 == 0) ans += max(0LL, x - f), x = min(x, f);
            if (c % 2 == 1) ans += max(0LL, l - x), x = max(x, l);
 
            if (c % 2 == 0) ans += l - x, x = l;
            if (c % 2 == 1) ans += x - f, x = f;
        }
    }
 
    if (end == n)
        end--;
 
    cout << ans - end << endl;
}