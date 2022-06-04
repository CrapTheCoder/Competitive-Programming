#include <bits/stdc++.h>
using namespace std;

#define endl '\n'
#define int long long
#define INF INT_MAX
#define MOD 1000000007

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int n, k; cin >> n >> k;

    int a[n];
    for (int i = 0; i < n; i++)
        cin >> a[i];

    bool dp[k+1] = {false};

    for (int i = 0; i <= k; i++) {
        for (int j = 0; j < n; j++) {
            if ((i - a[j] >= 0) && !dp[i - a[j]]) {
                dp[i] = true;
                break;
            }
        }
    }

    if (dp[k])
        cout << "First" << endl;
    else
        cout << "Second" << endl;
}
