#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
 
int n, m, k;
 
bool f(int x) {
    int c = 0;
    for (int i = 1; i <= n; i++)
        c += min(m, x/i);
 
    return c < k;
}
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    cin >> n >> m >> k;
 
    int l = 1, r = n*m;
    while (l < r) {
        int mid = l + (r - l) / 2;
        
        if (f(mid))
            l = mid + 1;
        else
            r = mid;
    }
 
    cout << r << endl;
}