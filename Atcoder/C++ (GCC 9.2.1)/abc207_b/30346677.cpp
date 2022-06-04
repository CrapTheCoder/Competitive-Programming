#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int a, b, c, d;
    cin >> a >> b >> c >> d;

    int count = 0;
    while (a + b * count > c * d * count) {
        if (count > 1e5) {
            cout << -1 << endl;
            return 0;
        }
        count++;
    }

    cout << count << endl;
}
