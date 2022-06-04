#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

int n, k;
pair<int, int> a[3013];

bool check(int c) {
    int dp[n]{};

    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            if (abs(a[i].second - a[j].second) >= c)
                dp[i] = max(dp[i], dp[j] + 1);

    return *max_element(dp, dp+n) >= k;
}

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int tc; cin >> tc;
    while (tc--) {
        cin >> n >> k;

        for (int i = 0; i < n; i++)
            cin >> a[i].first, a[i].second = i;
        
        int maxi = 0;
        for (int i = 0; i < n; i++)
            for (int j = 0; j <= i; j++)
                if (a[i].first == a[j].first)
                    maxi = max(maxi, abs(a[i].second - a[j].second));

        sort(a, a+n);
        int l = 0, r = n;
        while (l < r) {
            int m = (l+r+1) / 2;
            check(m) ? (l = m) : (r = m-1);
        }

        cout << max(maxi, l) << endl;
    }
}
