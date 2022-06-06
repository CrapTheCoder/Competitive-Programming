#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
#define all(iter) (iter).begin(), (iter).end()
#define rall(iter) (iter).rbegin(), (iter).rend()
#define size_of(iter) (int) (iter).size();
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int tc; cin >> tc;
    while (tc--) {
        int n; cin >> n;
        int arr[n];
        for (int i = 0; i < n; i++)
            cin >> arr[i];
 
        if (n < 3) {
            cout << 0 << endl;
            continue;
        }
 
        int minCost = n-1;
        for (int i = 0; i < n-1; i++) {
            for(int j = i + 1; j < n; j++) {
                long double delta = (long double) (arr[j] - arr[i]) / (j - i);
                int cost = 0;
 
                for(int k = 0; k < n; k++) {
                    if(k == i) continue;
                    if((arr[k] + delta * (i - k)) != arr[i]) cost++;
                }
                
                if(cost < minCost) minCost = cost;
            }
        }
 
        cout << minCost << endl;
    }
}