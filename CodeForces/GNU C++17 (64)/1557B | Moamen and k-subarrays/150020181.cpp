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
        int n, k; cin >> n >> k;
 
        pair<int, int> a[n];
        for (int i = 0; i < n; i++)
            cin >> a[i].first, a[i].second = i;
 
        sort(a, a+n);
 
        int count = 1;
        for (int i = 1; i < n; i++)
            if (a[i-1].second + 1 != a[i].second)
                count++;
 
        cout << (count <= k ? "YES" : "NO") << endl;
    }
}