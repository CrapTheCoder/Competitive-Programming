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
 
    int oc = count(a, a+n, 1);
 
    if (oc == n) {
        cout << oc - 1 << endl;
        return 0;
    }
 
    int gain[n];
    for (int i = 0; i < n; i++) {
        if (a[i] == 0) gain[i] = 1;
        if (a[i] == 1) gain[i] = -1;
    }
 
    int s = 0, mc = 0;
    for (int i = 0; i < n; i++) {
        s += gain[i];
        if (s < 0)
            s = 0;
 
        mc = max(mc, s);
    }
 
    cout << oc + mc << endl;
}