#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int n, m; cin >> n >> m;
 
    if (m == 0)
        cout << 1 << endl;
 
    else if (m <= n/2)
        cout << m << endl;
    
    else
        cout << n - m << endl;
}