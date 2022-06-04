#include <bits/stdc++.h>
using namespace std;

#define endl '\n'
#define INF numeric_limits::infinity()

#define speed ios::sync_with_stdio(false); cin.tie(NULL);

#define int long long

signed main(){
    speed;

    int t; cin >> t;

    while(t--){
        int n, k; cin >> n >> k;
        unordered_map<int, int> a;

        for(int i = 1; i <= k; i++)
            a[i] = -1;

        int maxi = 0;

        for(int i = 0; i < n; i++){
            int x; cin >> x;

            maxi = max(maxi, i - a[x] - 1);

            a[x] = i;
        }

        for(int i = 1; i <= k; i++)
            maxi = max(maxi, n - a[i] - 1);

        cout << maxi << endl;
    }
}
