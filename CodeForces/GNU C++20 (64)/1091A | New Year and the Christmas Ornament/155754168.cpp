#include <bits/stdc++.h>
using namespace std;
 
#define endl '\n'
#define int long long
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int a, b, c;
    cin >> a >> b >> c;
 
    cout << (min({a+2, b+1, c}) - 1) * 3 << endl;
}