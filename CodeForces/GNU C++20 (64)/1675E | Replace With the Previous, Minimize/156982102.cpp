#include <bits/stdc++.h>
using namespace std;
 
#define endl '\n'
#define int long long
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
signed main() {
//    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int tc; cin >> tc;
    while (tc--) {
        int n, k; cin >> n >> k;
        string s; cin >> s;
 
        int i; char c = 'a';
 
        for (i = 0; i < n; i++) {
            if (s[i] - 'a' <= k)
                c = max(c, s[i]);
            else
                break;
        }
 
        for (; c > 'a'; c--) {
            k--;
            for (int j = 0; j < n; j++)
                if (s[j] == c)
                    s[j]--;
        }
 
        while (k-- && s[i] > 'a') {
            c = s[i];
            for (int j = 0; j < n; j++)
                if (s[j] == c)
                    s[j]--;
        }
 
        cout << s << endl;
    }
}