#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
signed main() {
    int n; cin >> n;
    map<int, int> a;
 
    for (int i = 0; i < n; i++) {
        int x; cin >> x; a[x]++;
    }
 
    int dp[100013];
    dp[0] = 0; dp[1] = a[1];
 
    for (int i = 2; i < 100013; i++)
        dp[i] = max(dp[i-2] + i * a[i], dp[i-1]);
    
    cout << dp[100013 - 1] << endl;
}