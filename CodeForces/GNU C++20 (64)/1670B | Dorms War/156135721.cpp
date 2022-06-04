#include <bits/stdc++.h>
using namespace std;
 
signed main() {
    int tc; cin >> tc;
    while (tc--) {
        // Input
        
        int n; cin >> n;
        string s; cin >> s;
 
        set<char> v;
 
        int m; cin >> m;
        for (int i = 0; i < m; i++) {
            char x; cin >> x;
            v.insert(x);
        }
        
        // Algo
        
        int maxi = 0, non = 0;
        bool flag = false;
        
        for (auto i : s) {
            if (v.contains(i)) {
                maxi = max(maxi, non + flag);
                non = 0; flag = true;
                
            } else {
                non++;
            }
        }
        
        cout << maxi << endl;
    }
}