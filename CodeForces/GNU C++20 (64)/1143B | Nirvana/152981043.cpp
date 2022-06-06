#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    string s; cin >> s;
 
    int f = 1, maxi = pow(9, s.size() - 1);
    for (int i = 0; i < s.size(); i++) {
        if (s[i] != '0') {
            int nw = f * (s[i]-'0'-1) * pow(9, s.size()-i-1);
            if (maxi < nw) maxi = nw;
        }
 
        f *= s[i]-'0';
    }
 
    cout << max(maxi, f) << endl;
}