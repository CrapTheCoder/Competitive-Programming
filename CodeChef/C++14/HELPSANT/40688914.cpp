#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

signed main()
{
    ios::sync_with_stdio(false); cin.tie(NULL);

    int n; cin >> n;

    set<int> s;
    for (int i = 0; i < n; i++) {
        int x; cin >> x;
        s.insert(x);
    }

    for (auto i : s)
        cout << i << " ";

    cout << endl;
}
