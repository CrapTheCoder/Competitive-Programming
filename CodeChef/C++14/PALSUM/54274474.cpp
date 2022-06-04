#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;

bool pal(int n) {
    string s;
    for (int i = 0; (n >> i) > 0; i++)
        s += ((n >> i) & 1) + '0';
    
    string s2 = s;
    reverse(s2.begin(), s2.end());
    
    return s == s2;
}

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    pair<int, int> p[1013];
    p[1] = {1, 0};

    set<int> pals;
    for (int i = 1; i < 1013; i++)
        if (pal(i))
            pals.insert(i);

    for (int i = 2; i < 1013; i++) {
        p[i] = {INF, -1};

        if (pals.count(i))
            p[i] = {1, 0};

        for (int j = i-1; j >= 1; j--)
            if (pals.count(i - j))
                if (p[j].first + 1 < p[i].first)
                    p[i] = {p[j].first + 1, j};
    }

    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        vector<int> d;

        while (n) {
            d.push_back(n - p[n].second);
            n = p[n].second;
        }

        cout << d.size() << endl;
        for (auto i : d)
            cout << i << " ";
        
        cout << endl;
    }
}
