#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int n, x;
    cin >> n >> x;

    int a[n+1];
    for (int i = 1; i <= n; i++)
        cin >> a[i];

    while (a[x] != -1) {
        int y = x;
        x = a[x];
        a[y] = -1;
    }

    cout << count(a+1, a+n+1, -1) << endl;
}
