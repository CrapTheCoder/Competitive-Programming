#include<bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'
#define speed ios::sync_with_stdio(false); cin.tie(NULL);

signed main(){
    speed;

    int t; cin >> t;

    while(t--){
        int n; cin >> n;
        int a[n];

        for(int i = 0; i < n; i++)
            cin >> a[i];

        cout << *max_element(a, a + n) << endl;
    }
}
