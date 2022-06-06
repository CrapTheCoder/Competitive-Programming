#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
 
const int INF = LLONG_MAX >> 1;
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int tc; cin >> tc;
 
    while (tc--) {
        int n; cin >> n;
        
        int a[n][6] = {0};
        for (int i = 0; i < n; i++) {
            string s; cin >> s;
            for (auto j : s)
                a[i][j-'a']++;
            
            a[i][5] = s.size();
        }
 
        int maxi = 0;
        
        for (int j = 0; j < 5; j++) {
            pair<int, int> b[n];
            for (int i = 0; i < n; i++) {
                int x = a[i][j], y = a[i][5] - a[i][j];
 
                b[i] = {x - y, i};
            }
 
            sort(b, b+n, greater<pair<int, int>>());
 
            int s1 = 0, s2 = 0, c = 0;
 
            for (int k = 0; k < n; k++) {
                int i = b[k].second;
                int x = a[i][j], y = a[i][5] - a[i][j];
 
                s1 += x;
                s2 += y;
 
                if (s1 <= s2) {
                    s1 -= x;
                    s2 -= y;
                } else
                    c++;
            }
 
            maxi = max(maxi, c);
        }
 
        cout << maxi << endl;
    }
}