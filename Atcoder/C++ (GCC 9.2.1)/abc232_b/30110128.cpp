#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int h, w;
    cin >> h >> w;

    int a[h+1][w+1];
    for (int i = 1; i <= h; i++)
        for (int j = 1; j <= w; j++)
            cin >> a[i][j];

    for (int i1 = 1; i1 <= h; i1++) {
        for (int i2 = i1+1; i2 <= h; i2++) {
            for (int j1 = 1; j1 <= w; j1++) {
                for (int j2 = j1+1; j2 <= w; j2++) {
                    if (a[i1][j1] + a[i2][j2] > a[i2][j1] + a[i1][j2]) {
                        cout << "No" << endl;
                        return 0;
                    }
                }
            }
        }
    }

    cout << "Yes" << endl;
}
