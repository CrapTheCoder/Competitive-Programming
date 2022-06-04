#include <bits/stdc++.h>
using namespace std;

typedef int f;

typedef long long int ll;
#define int ll

int log_(int n){
    int x = 1;
    int c = 0;

    while(true){
        x *= 2;

        if(x > n)
            break;

        c++;
    }

    return c;
}

int solve(ll p, int idx){
    if(idx <= 0)
        return 0;

    int d = log_(idx);

    return pow(2, p - d - 1) + solve(p, idx - pow(2, d));
}

f main(){
    int t; cin >> t;

    while(t--){
        int p, idx; cin >> p >> idx;

        cout << solve(p, idx) << endl;
    }
}
