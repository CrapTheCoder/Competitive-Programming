#include <bits/stdc++.h>
using namespace std;

signed main() {
    int n; cin >> n;
    vector<int> d = {0};

    int cur = 0;
    for (int i = 0; i < n; i++) {
        int x; cin >> x;
        cur = (x + cur) % 360;
        d.push_back(cur);
    }

    sort(d.begin(), d.end());

    int maxi = 360 - d.back();
    for (int i = 1; i < d.size(); i++)
        if (d[i] - d[i-1] > maxi)
            maxi = d[i] - d[i-1];

    cout << maxi << endl;
}
