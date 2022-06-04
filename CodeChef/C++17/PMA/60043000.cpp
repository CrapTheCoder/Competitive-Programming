#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int tc; cin >> tc;

    while (tc--) {
        int n; cin >> n;

        int a[n];
        for (int i = 0; i < n; i++) {
            cin >> a[i]; a[i] = abs(a[i]);
        }

        vector<int> pos, neg;
        for (int i = 0; i < n; i++) {
            if ((i+1) % 2 == 1) pos.push_back(a[i]);
            if ((i+1) % 2 == 0) neg.push_back(a[i]);
        }

        int sum = 0;
        for (auto i : pos) sum += i;
        for (auto i : neg) sum -= i;

        int min_pos = *min_element(pos.begin(), pos.end());
        int max_neg = *max_element(neg.begin(), neg.end());

        int new_sum = sum - min_pos + max_neg;
        new_sum -= min_pos;
        new_sum += max_neg;

        cout << max(sum, new_sum) << endl;
    }
}
