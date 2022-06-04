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

        multiset<int> s;
        for (int i = 0; i < n; i++) {
            int x; cin >> x;
            s.insert(x);
        }

        int count = 0;
        while (true) {
            int v = *s.rbegin();
            if (v == 0) {
                count = INF;
                break;
            }

            z -= v, count++;
            if (z <= 0) break;

            s.erase(s.find(v));
            s.insert(v / 2);
        }

        if (count == INF)
            cout << "Evacuate" << endl;
        else
            cout << count << endl;
    }
}
