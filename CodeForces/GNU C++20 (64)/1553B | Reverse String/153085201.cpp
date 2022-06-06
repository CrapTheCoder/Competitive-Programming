#include <bits/stdc++.h>
using namespace std;
 
signed main() {
    int tc; cin >> tc;
    while (tc--) {
        string s, t; cin >> s >> t;
        int n = s.size(), m = t.size();
 
        bool poss = false;
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                string res;
                
                // Left
                for (int l = i; l < j; l++)
                    res += s[l];
 
                // Right
                for (int l = j; l >= j-(m-(j-i+1)); l--) {
                    if (l < 0) goto skip;
                    res += s[l];
                }
 
                if (res == t)
                    poss = true;
                
                skip:;
            }
        }
 
        cout << (poss ? "YES" : "NO") << endl;
    }
}