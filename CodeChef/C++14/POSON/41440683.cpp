#include <bits/stdc++.h>

using namespace std;

#define endl '\n'
#define int long long

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
    int t; cin >> t;

    while (t--) {
        string s, t; cin >> s >> t;

        if (s.size() != t.size()) {
            cout << "No" << endl;
            continue;
        }

        int sa = 0, sb = 0;
        int ta = 0, tb = 0;

        for (auto i : s) {
            if (i == 'a') sa++;
            if (i == 'b') sb++;
        }

        for (auto i : t) {
            if (i == 'a') ta++;
            if (i == 'b') tb++;
        }

        if ((sa != ta) || (sb != tb)) {
            cout << "No" << endl;
            continue;
        }

        int c = 0;
        for (int i = 0; i < s.size(); i++)
            if (s[i] != t[i])
                c++;

        cout << "Yes " << c / 2 << endl;
    }
}
