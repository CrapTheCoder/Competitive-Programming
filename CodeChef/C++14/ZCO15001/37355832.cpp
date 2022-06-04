#include <bits/stdc++.h>
using namespace std;

#define endl '\n'
#define INF (INT_MAX / 2)

int main() {
    int n; cin >> n;
    int a[n];

    for (int i = 0; i < n; i++)
        cin >> a[i];

    int dp[n + 1];
    fill(dp, dp + n + 1, INF);

    dp[0] = 0;

    for (int i = 0; i < n; i++) {
        for (int j = -1; j < i; j++) {
            bool is_pal = true;

            for (int k1 = j+1, k2 = i; k1 < k2; k1++, k2--) {
                if (a[k1] != a[k2]) {
                    is_pal = false;
                    break;
                }
            }

            // cout << dp[i] << " " << dp[j] << endl;

            if (is_pal)
                dp[i+1] = min(dp[i+1], dp[j+1] + 1);
        }
    }

    cout << dp[n] << endl;
}
