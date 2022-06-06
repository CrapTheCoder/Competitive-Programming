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
        s += "~";
 
        int cur_count = 1;
 
        set<char> ans;
        for (int i = 1; i < s.size(); i++) {
            if (s[i] == s[i-1])
                cur_count++;
 
            else {
                if (cur_count % 2 == 1)
                    ans.insert(s[i-1]);
 
                cur_count = 1;
            }
        }
 
        for (auto i : ans)
            cout << i;
        cout << endl;
    }
}