#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int n; cin >> n;
    
    int a[n];
    for (int i = 0; i < n; i++)
        cin >> a[i];
    
    map<int, int> dp;
    for (int i = 0; i < n; i++)
        dp[a[i]] = max(dp[a[i]], dp[a[i]-1] + 1);
    
    int maxi = 0, maxv = -1;
    for (auto [x, y] : dp)
        if (y > maxi)
            maxv = x, maxi = y;
 
    vector<int> inds;
    for (int i = n-1; i >= 0; i--)
        if (a[i] == maxv)
            maxv--, inds.push_back(i+1);
 
    reverse(inds.begin(), inds.end());
 
    cout << maxi << endl;
    for (auto i : inds)
        cout << i << " ";
}