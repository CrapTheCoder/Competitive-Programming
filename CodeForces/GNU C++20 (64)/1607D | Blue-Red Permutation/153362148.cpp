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
         int n; cin >> n;
         int a[n];
         for (int i = 0; i < n; i++)
             cin >> a[i];
 
         vector<int> b, r;
 
         string s; cin >> s;
         for (int i = 0; i < n; i++) {
             if (s[i] == 'B') b.push_back(a[i]);
             if (s[i] == 'R') r.push_back(a[i]);
         }
 
         bool flag = false;
 
         int j = 0;
 
         sort(b.begin(), b.end());
         for (; j < b.size(); j++)
             if (b[j] < j+1)
                 flag = true;
 
        sort(r.begin(), r.end());
        for (; j < n; j++)
            if (r[j - b.size()] > j+1)
                flag = true;
 
         if (flag)
             cout << "NO" << endl;
         else
             cout << "YES" << endl;
    }
}