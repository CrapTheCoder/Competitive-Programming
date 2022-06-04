#include <bits/stdc++.h>
using namespace std;
 
#define int long long
 
signed main() {
    int n, k; cin >> n >> k;
 
    multiset<int> s;
    for (int i = 0; i < n; i++) {
        int x; cin >> x;
        s.insert(x);
    }
 
    while (true) {
        auto x = *s.begin();
        if (x > 0 || k == 0) break;
 
        s.erase(s.begin());
        s.insert(-x);
        k--;
    }
 
    if (k % 2) {
        auto x = *s.begin();
        s.erase(s.begin());
        s.insert(-x);
    }
 
    cout << accumulate(s.begin(), s.end(), 0) << endl;
}