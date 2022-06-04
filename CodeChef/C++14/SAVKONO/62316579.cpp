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
        int n, z; cin >> n >> z;

        vector<int> a;
        for (int i = 0; i < n; i++) {
            int x; cin >> x;

            while (x) {
                a.push_back(x);
                x /= 2;
            }
        }

        sort(a.begin(), a.end());

        int count = 0;
        for (int i = a.size() - 1; i >= 0; i--) {
            z -= a[i]; count++;
            if (z <= 0) break;
        }

        if (z > 0)
            cout << "Evacuate" << endl;
        else
            cout << count << endl;
    }
}
