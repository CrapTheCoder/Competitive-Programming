#include <bits/stdc++.h>
using namespace std;
 
signed main() {
    int n; cin >> n;
    map<int, int> a;
    for (int i = 0; i < n; i++) {
        int x; cin >> x; a[x]++;
    }
 
    map<int, int> c;
    for (auto [x, y]: a)
        c[y]++;
 
    int q; cin >> q;
    while (q--) {
        char t; int x;
        cin >> t >> x;
 
        c[a[x]]--;
        if (t == '-') a[x]--;
        if (t == '+') a[x]++;
        c[a[x]]++;
 
        bool square = false;
        int pair_count = 0;
 
        for (auto [i, j]: c) {
            pair_count += i/2 * j;
            if (i >= 4 && j > 0 && !square) {
                pair_count -= 2;
                square = true;
            }
        }
 
        cout << ((square && pair_count >= 2) ? "YES" : "NO") << endl;
    }
}