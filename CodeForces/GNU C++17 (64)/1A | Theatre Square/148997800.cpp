#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int n, m, a;
    cin >> n >> m >> a;
 
    cout << ((n+a-1) / a) * ((m+a-1) / a) << endl;
}