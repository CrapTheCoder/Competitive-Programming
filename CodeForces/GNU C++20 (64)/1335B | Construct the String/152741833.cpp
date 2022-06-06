#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
const string alps = "abcdefghijklmnopqrstuvwxyz";
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int tc; cin >> tc;
    while (tc--) {
        int n, a, b;
        cin >> n >> a >> b;
 
        string res;
        for (int i = 0; i < n; i++)
            res += alps[i%b];
 
        cout << res << endl;
    }
}