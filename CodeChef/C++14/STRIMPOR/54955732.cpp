#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'
#define all(iter) (iter).begin(), (iter).end()
#define rall(iter) (iter).rbegin(), (iter).rend()

const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int tc; cin >> tc;
    while (tc--) {
        int n, k;
        cin >> n >> k;

        char a[n];
        for (int i = 0; i < n; i++)
            cin >> a[i];

        int xs[n], zs[n];
        memset(xs, 0, sizeof xs);
        memset(zs, 0, sizeof zs);

        int curx[3] = {0, 0, 0}, curz[3] = {0, 0, 0};

        for (int i = 0; i < n; i++) {
            if (a[i] == 'X') curx[i%3]++;
            if (a[i] == 'Z') zs[i] = curx[(i+1) % 3];
        }

        for (int i = n-1; i >= 0; i--) {
            if (a[i] == 'Z') curz[i%3]++;
            if (a[i] == 'X') xs[i] = curz[(i+2) % 3];
        }
        
        int val = 0;
        for (int i = 0; i < k; i++)
            val += xs[i];

        int mini = val;
        for (int i = k; i < n; i++) {
            val += xs[i];
            val -= zs[i-k];
            mini = min(mini, val);
        }
        
        cout << mini << endl;
    }
}