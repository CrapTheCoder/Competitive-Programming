#include <bits/stdc++.h>
using namespace std;
 
signed main() {
    int n; cin >> n;
 
    int time = 0, prev = 0;
    for (int i = 1; i <= n; i++) {
        int cur; cin >> cur;
        time += abs(cur - prev);
        prev = cur;
    }
 
    cout << time + n + (n-1) << endl;
}