#include <bits/stdc++.h>
using namespace std;
 
signed main() {
    int n, k; cin >> n >> k;
 
    multiset<int> s;
    for (int i = 0; i < n; i++) {
        int x; cin >> x;
        s.insert(x);
    }
 
    while (k--) {
        auto x = *s.begin();
        s.erase(s.begin());
        s.insert(-x);
    }
 
    cout << accumulate(s.begin(), s.end(), 0) << endl;
}