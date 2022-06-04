#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int tc; cin >> tc;
    while (tc--) {
        int n; cin >> n;
        int cnt[4]{};

        int ans = 0, total = 0;

        for (int i = 0; i < n; i++) {
            int x; cin >> x;
            cnt[x % 4]++;

            total += x;
        }

        if (total % 4 != 0) {
            cout << -1 << endl;
            continue;
        }

        int fs = min(cnt[1], cnt[3]);
        ans += fs; cnt[1] -= fs; cnt[3] -= fs;

        ans += (cnt[1] / 2) + (cnt[3] / 2);
        cnt[2] += (cnt[1] / 2) + (cnt[3] / 2);
        cnt[1] = cnt[3] = 0;

        ans += cnt[2] / 2;

        cout << ans << endl;
    }
}
