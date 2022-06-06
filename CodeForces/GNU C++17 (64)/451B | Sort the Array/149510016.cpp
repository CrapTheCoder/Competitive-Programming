#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int n; cin >> n;
    vector<int> a(n), b(n);
    for (int i = 0; i < n; i++)
        cin >> a[i], b[i] = a[i];
 
    sort(b.begin(), b.end());
 
    int l, r;
 
    for (l = 0; l < n; l++)
        if (a[l] != b[l])
            break;
 
    for (r = n-1; r >= 0; r--)
        if (a[r] != b[r])
            break;
 
    if (l > r)
        cout << "yes\n" << 1 << " " << 1 << endl;
 
    else {
        reverse(a.begin() + l, a.begin() + r + 1);
        if (a == b)
            cout << "yes\n" << l+1 << " " << r+1 << endl;
        else
            cout << "no" << endl;
    }
}