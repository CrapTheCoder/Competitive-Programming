#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
int f(int a, int x) {
    return x / a + x % a;
}
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int tc; cin >> tc;
 
    while (tc--) {
        int l, r, a;
        cin >> l >> r >> a;
 
        int x = r - r%a - 1;
 
        if (l <= x)
            cout << max(f(a, r), f(a, x)) << endl;
        else
            cout << f(a, r) << endl;
    }
}