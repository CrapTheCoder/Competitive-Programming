#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

const int MOD = 1e9 + 7;
const int MAX = 1e6 + 13;

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int n, d; cin >> n >> d;
    pair<int, int> p[n];

    for (int i = 0; i < n; i++)
        cin >> p[i].first >> p[i].second;
    
    sort(p, p+n);
    
    int c = 0;
    for (int i = 0; i < n;) {
        int mini = p[i++].second; c++;
        while (i < n && p[i].first < mini + d)
            mini = min(mini, p[i++].second);
    }

    cout << c << endl;
}
