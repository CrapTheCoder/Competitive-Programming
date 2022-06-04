#include <bits/stdc++.h>
using namespace std;

signed main() {
    int n; cin >> n;
    
    int a[n];
    for (int i = 0; i < n; i++)
        cin >> a[i];
    
    unordered_set<int> s;
    for (int i = 0; i < n; i++) {
        if (s.count(a[i]))
            s.erase(a[i]);
        else
            s.insert(a[i]);
    }

    cout << s.size() << endl;
}
