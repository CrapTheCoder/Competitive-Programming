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
        int n, k; cin >> n >> k;
        if ((n % 2 != k % 2) || (k*k > n))
            cout << "NO" << endl;
 
        else
            cout << "YES" << endl;
    }
}