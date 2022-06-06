#include <bits/stdc++.h>
using namespace std;
#define int long long
#define endl '\n'
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int tc; cin >> tc;
 
    while (tc--) {
        int n; cin >> n;
 
        int s = 0;
        int maxi = 0;
        int maxii = 0;
 
        int a[n];
        for (int i = 0; i < n; i++) {
            cin >> a[i];
            s += a[i];
 
            if (maxi < a[i]) {
                maxi = a[i];
                maxii = i;
            }
        }
 
        s -= a[maxii];
        a[maxii] = min(a[maxii], s);
        s += a[maxii];
 
        cout << s / 2 << endl;
 
        priority_queue<pair<int, int>> pq;
        for (int i = 0; i < n; i++) {
            pair<int, int> p = {a[i], i+1};
            pq.emplace(p);
        }
 
        while (true) {
            pair<int, int> x = pq.top(); pq.pop();
            pair<int, int> y = pq.top(); pq.pop();
 
            if (x.first == 0 || y.first == 0)
                break;
 
            x.first--; y.first--;
 
            cout << x.second << " " << y.second << endl;
 
            pq.emplace(x);
            pq.emplace(y);
        }
    }
}