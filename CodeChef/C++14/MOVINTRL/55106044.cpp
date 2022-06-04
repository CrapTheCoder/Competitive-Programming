#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'
#define all(iter) (iter).begin(), (iter).end()
#define rall(iter) (iter).rbegin(), (iter).rend()
#define size_of(iter) (int) iter.size();

const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;

int c, n, k;
pair<int, int> a[100013];

bool solve(int ind) {
    int maxi = 0, prev = 0;
    for (int i = 1; i <= n; i++) {
        if (i == ind)
            continue;
        
        if (a[i].first <= a[prev].second)
            return false;
        
        maxi = max(maxi, a[i].first - a[prev].second - 1);
        prev = i;
    }

    return maxi >= a[ind].second - a[ind].first + 1;
}

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int tc; cin >> tc;
    while (tc--) {
        cin >> c >> n >> k;

        a[0].first = 0; a[0].second = 0;
        for (int i = 1; i <= n; i++)
            cin >> a[i].first >> a[i].second;
        
        sort(a, a+n+1);

        int ind = -1;
        for (int i = 1; i < n; i++) {
            if (a[i+1].first <= a[i].second) {
                ind = i;
                break;
            }
        }

        if (ind == -1) {
            cout << "Good" << endl;
            continue;
        }

        if (k == 0) {
            cout << "Bad" << endl;
            continue;
        }
        
        cout << (solve(ind) || solve(ind+1) ? "Good" : "Bad") << endl;
    }
}
