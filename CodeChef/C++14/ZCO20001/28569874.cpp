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

ll solve(ll p, ll idx){
    if(idx <= 0)
        return 0;

    ll d = log_(idx);

    return pow(2, p - d - 1) + solve(p, idx - pow(2, d));
}

int main(){
    ll t; cin >> t;

    while(t--){
        ll p, idx; cin >> p >> idx;

        cout << solve(p, idx) << endl;
    }
}
