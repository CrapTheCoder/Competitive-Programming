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
        int n; cin >> n;
        int c = 0;
 
        while (n % 3 == 0 && n % 2 == 0)
            n /= 6, c++;
 
        while (n % 3 == 0)
            n /= 3, c += 2;
 
        if (n == 1)
            cout << c << endl;
        else
            cout << -1 << endl;
    }
}