#include <bits/stdc++.h>
using namespace std;
 
int n, b[2000013], p[2000013], weight[2000013], weight_sum[2000013];
 
bool assign() {
    for (int i = 0, cur_weight = 0; i < n; i++) {
        int cur = p[i], par = b[p[i]];
 
        if (cur == par) {
            weight[cur] = 0;
            continue;
        }
 
        if (weight[par] == -1)
            return false;
        
        weight[cur] = ++cur_weight - weight_sum[par];
        weight_sum[cur] = weight_sum[par] + weight[cur];
    }
 
    return true;
}
 
signed main() {
    int tc; cin >> tc;
    while (tc--) {
        cin >> n; fill(weight, weight + n, -1);; fill(weight_sum, weight_sum + n, 0);
        for (int i = 0; i < n; i++) {cin >> b[i]; b[i]--;}
        for (int i = 0; i < n; i++) {cin >> p[i]; p[i]--;}
 
        if (!assign()) {
            cout << -1 << endl;
            
        } else {
            for (int i = 0; i < n; i++)
                cout << weight[i] << " ";
            cout << endl;
        }
    }
}