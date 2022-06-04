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
        int n, k; cin >> n >> k;
        int b[n]; vector<int> a;

        for (int i = 0; i < n; i++) {
            cin >> b[i]; b[i]--;
            if (i == 0 || b[i] != b[i-1])
                a.push_back(b[i]);
        }

        n = a.size();

        int tot[k] = {0};

        for (int i = 0; i < n; i++) {
            int c = 2;
            if (i == 0) c--;
            if (i == n-1) c--;

            if (i > 0 && i < n-1 && a[i-1] != a[i+1]) {
                c--;
            }

            tot[a[i]] += c;
        }

        for (int i = 0; i < k; i++)
            cout << (n-1) - tot[i] << " ";
        
        cout << endl;
    }
}
