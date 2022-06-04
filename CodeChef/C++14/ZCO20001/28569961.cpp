#include <bits/stdc++.h>
using namespace std;

typedef long long int ll;

ll log_(ll n){
    ll x = 1;
    ll c = 0;

    while(true){
        x *= 2;

        if(x > n)
            break;

        c++;
    }

    return c;
}

int main(){
    ll t; cin >> t;

    while(t--){
        ll p, idx; cin >> p >> idx;

        ll ans = 0;

        while(idx > 0){
            int d = log_(idx);

            ans += pow(2, p - d - 1);

            idx -= pow(2, d);
        }

        cout << ans << endl;
    }
}
