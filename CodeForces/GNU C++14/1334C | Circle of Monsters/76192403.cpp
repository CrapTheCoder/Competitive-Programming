#include<bits/stdc++.h>
using namespace std;
 
#define INF LLONG_MAX
 
#define endl '\n'
#define int long long
 
signed main()
{
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int t; cin >> t;
 
    while(t--){
        int n; cin >> n;
 
        int s = 0;
 
        int x[n][2];
 
        for(int i = 0; i < n; i++){
            cin >> x[i][0] >> x[i][1];
            s += x[i][0];
        }
 
        int m = 0;
        int ms = INF;
 
        for(int i = 0; i < n; i++){
            x[i][1] = min(x[i][1], x[(i+1)%n][0]);
 
            m += x[i][1];
            ms = min(ms, x[i][1]);
        }
 
        cout << s - (m - ms) << endl;
    }
}