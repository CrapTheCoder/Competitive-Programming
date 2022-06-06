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
 
        int a[n] = {0};
        for (int i = 1; i < n; i++)
            cin >> a[i], a[i]--;
 
        string s; cin >> s;
 
        int c = 0;
        pair<int, int> f[n];
        for (int i = n-1; i >= 0; i--) {
            if (s[i] == 'W') f[i].first++;
            if (s[i] == 'B') f[i].second++;
 
            if (f[i].first == f[i].second)
                c++;
 
            f[a[i]].first += f[i].first;
            f[a[i]].second += f[i].second;
        }
 
        cout << c << endl;
    }
}