#include <bits/stdc++.h>
 
using namespace std;
 
#define endl '\n'
#define int long long
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
    int t; cin >> t;
 
    while (t--) {
        int n, m; cin >> n >> m;
        int k[n], c[m];
 
        for (int i = 0; i < n; i++) {
            cin >> k[i];
            k[i]--;
        }
 
        for (int i = 0; i < m; i++)
            cin >> c[i];
 
        sort(k, k+n);
 
        int j = 0, s = 0;
 
        for (int p = n-1; p >= 0; p--) {
            int i = k[p];
 
            if (j > i)
                s += c[i];
 
            else {
                s += c[j];
                j++;
            }
        }
 
        cout << s << endl;
    }
}