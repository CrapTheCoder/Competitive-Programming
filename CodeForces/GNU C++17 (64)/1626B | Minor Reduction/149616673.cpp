#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
void solution() {
    string s; cin >> s;
    int n = s.size();
 
    for (int i = n-2; i >= 0; i--) {
        int t = (s[i] - '0') + (s[i + 1] - '0');
        if (t > 9) {
            s[i] = t / 10 + '0';
            s[i+1] = t % 10 + '0';
            cout << s << endl;
 
            return;
        }
    }
 
    int t = (s[0] - '0') + (s[1] - '0');
    s[1] = t + '0';
 
    cout << s.substr(1, n-1) << endl;
}
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int tc; cin >> tc;
    while (tc--)
        solution();
}