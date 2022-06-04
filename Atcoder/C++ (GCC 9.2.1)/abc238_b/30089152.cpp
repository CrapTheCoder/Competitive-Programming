#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int n; cin >> n;
    vector<int> cut_degrees = {0, 360};

    int cur = 0;
    for (int i = 0; i < n; i++) {
        int x; cin >> x;
        cur = (x + cur) % 360;
        cut_degrees.push_back(cur);
    }

    sort(cut_degrees.begin(), cut_degrees.end());

    int maxi = 0;
    for (int i = 1; i < cut_degrees.size(); i++)
        maxi = max(maxi, cut_degrees[i] - cut_degrees[i-1]);

    cout << maxi << endl;
}
