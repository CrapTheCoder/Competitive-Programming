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
        string s; cin >> s;
 
        if (k * 2 == n) {
            cout << "NO" << endl;
            continue;
        }
 
        string s1 = s.substr(0, k);
        string s2 = s.substr(s.size() - k, k);
        reverse(s2.begin(), s2.end());
 
        if (s1 == s2)
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
}