#include <bits/stdc++.h>
using namespace std;
 
#define endl '\n'
#define int long long
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int n; cin >> n;
    string s; cin >> s;
 
    char m = s[0];
    int mi = 0;
 
    for (int i = 1; i < n; i++) {
        if (m > s[i]) {
            cout << "YES" << endl;
            cout << mi+1 << " " << i+1 << endl;
            return 0;
 
        } else {
            m = s[i];
            mi = i;
        }
    }
 
    cout << "NO" << endl;
}