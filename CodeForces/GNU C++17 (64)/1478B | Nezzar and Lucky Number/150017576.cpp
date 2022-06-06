#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
void solve(int n, int d) {
    if (n >= 10*d) {
        cout << "YES" << endl;
        return;
    }
 
    while (n >= 0) {
        n -= d;
        if (n % 10 == 0) {
            cout << "YES" << endl;
            return;
        }
    }
 
    cout << "NO" << endl;
}
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int tc; cin >> tc;
    while (tc--) {
        int n, d; cin >> n >> d;
        while (n--) {
            int x; cin >> x;
            solve(x, d);
        }
    }
}