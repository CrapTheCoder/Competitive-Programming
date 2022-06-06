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
 
        map<char, int> mp;
        for (int i = 0; i < s.size(); i++)
            mp[s[i]]++;
 
        for (int i = 0; i < s.size(); i++) {
            if (mp[s[i]] == 1) {
                cout << s.substr(i, s.size()) << endl;
                break;
            }
 
            mp[s[i]]--;
        }
    }
}