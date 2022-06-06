#include <bits/stdc++.h>
using namespace std;
    
#define int long long
#define endl '\n'
    
int n, root;
int b[200013], p[200013], weight[200013], weight_sum[200013];
    
bool assign() {
    int maxi = 0;
    
    for (int i = 0; i < n; i++) {
        int cur = p[i];
        int par = b[cur];
    
        if (cur == par) {
            weight[cur] = 0;
            continue;
        }
    
        if (weight[par] == -1)
            return false;
        
        weight[cur] = ++maxi - weight_sum[par];
        weight_sum[cur] = weight[cur] + weight_sum[par];
    }
    
    return true;
}
    
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
    
    int tc; cin >> tc;
    while (tc--) {
        cin >> n; fill(weight, weight + n, -1); fill(weight_sum, weight_sum + n, 0);
        for (int i = 0; i < n; i++) {cin >> b[i]; b[i]--;}
        for (int i = 0; i < n; i++) {cin >> p[i]; p[i]--;}
    
        if (!assign()) {
            cout << -1 << endl;
            continue;
        }
    
        bool flag = false;
        for (int i = 0; i < n; i++)
            if (weight[i] == -1)
                flag = true;
        
        if (flag) {
            cout << -1 << endl;
            continue;
        }
        
        for (int i = 0; i < n; i++)
            cout << weight[i] << " ";
        cout << endl;
    }
}