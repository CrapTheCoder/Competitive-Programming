#include <bits/stdc++.h>
using namespace std;
 
#define endl '\n'
#define int long long
 
signed main() {
    // ios::sync_with_stdio(false); cin.tie(NULL);
 
    int tc; cin >> tc;
    while (tc--) {
        int n; char c;
        cin >> n >> c;
        string s; cin >> s;
 
        vector<int> f, g;
 
        for (int i = 0; i < n; i++) {
            if (s[i] != c)
                f.push_back(i+1);
            else
                g.push_back(i+1);
        }
 
        if (f.size() == 0) {
            cout << 0 << endl;
            continue;
        }
 
        bool flag2 = false;
        for (auto i : g) {
            bool flag = false;
            for (auto j : f) {
                if (j % i == 0) {
                    flag = true;
                    break;
                }
            }
 
            if (!flag) {
                flag2 = true;
                cout << 1 << endl;
                cout << i << endl;
                break;
            }
        }
 
        if (!flag2) {
            cout << 2 << endl;
            cout << n << " " << n-1 << endl;
        }
    }
}