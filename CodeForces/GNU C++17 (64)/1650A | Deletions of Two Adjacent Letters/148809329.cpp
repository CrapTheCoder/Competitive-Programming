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
        string s; cin >> s;
        char c; cin >> c;
 
        bool flag = false;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == c && i % 2 == 0)
                flag = true;
        }
 
        cout << (flag ? "YES" : "NO") << endl;
    }
}