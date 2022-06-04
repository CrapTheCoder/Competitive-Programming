#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'
#define all(iter) (iter).begin(), (iter).end()
#define rall(iter) (iter).rbegin(), (iter).rend()
#define size_of(iter) (int) (iter).size();

const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int n; cin >> n;
    int a[n+1]; for (int i = 1; i <= n; i++) cin >> a[i];
    int b[n+1]; for (int i = 1; i <= n; i++) cin >> b[i];

    int p[n+2] = {0}; for (int i = 1; i <= n; i++) p[i] = p[i-1] + b[i];
    int s[n+2] = {0}; for (int i = n; i >= 1; i--) s[i] = s[i+1] + b[i];
    
    int maxi = *max_element(a+1, a+n+1);

    int x[n+1]; fill(x, x+n+1, -INF);
    for (int i = 1; i <= n; i++)
        x[i] = max(x[i-1], a[i] - p[i]);
    
    for (int i = 1; i <= n; i++)
        maxi = max(maxi, a[i] + p[i-1] + x[i-1]);
    
    int y[n+1]; fill(y, y+n+1, -INF);
    for (int i = 1; i <= n; i++)
        y[i] = max(y[i-1], a[i] + p[i-1]);
    
    for (int i = 1; i <= n; i++)
        maxi = max(maxi, a[i] + s[i+1] + y[i-1]);
    
    cout << maxi << endl;
}
