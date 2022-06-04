#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int n; cin >> n;
    int a[n][2];

    for (int i = 0; i < n; i++)
        cin >> a[i][0] >> a[i][1];

    double maxi = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int d1 = abs(a[i][0] - a[j][0]);
            int d2 = abs(a[i][1] - a[j][1]);

            maxi = max(maxi, sqrt(d1*d1 + d2*d2));
        }
    }

    cout << fixed << setprecision(10) << maxi << endl;
}
