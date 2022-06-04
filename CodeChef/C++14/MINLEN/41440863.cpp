#include <bits/stdc++.h>

using namespace std;

#define endl '\n'
#define int long long

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
    int t; cin >> t;

    while (t--) {
        string s; cin >> s;

        stack<char> ns;

        for (auto i : s) {
            if (ns.empty()) {
                ns.push(i);
                continue;
            }

            if (ns.top() == i) {
                ns.pop();
                continue;
            }

            ns.push(i);
        }

        cout << ns.size() << endl;
    }
}
