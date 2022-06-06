#include <bits/stdc++.h>
using namespace std;
 
#define endl '\n'
#define int long long
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int tc; cin >> tc;
    while (tc--) {
        int n; cin >> n;
 
        int f = 1;
        vector<int> a;
        bool flag = false;
 
        for (int i = 0; i < n; i++) {
            a.push_back(f);
            if (f > 1e9) {
                flag = true;
                break;
            }
 
            f *= 3;
        }
 
        if (flag)
            cout << "NO" << endl;
 
        else {
            cout << "YES" << endl;
            for (auto i : a)
                cout << i << " ";
            cout << endl;
        }
    }
}