#include <bits/stdc++.h>
using namespace std;
#define MAXN 100000
#define MOD 1000000007

typedef long long int ll;

ll facts[MAXN + 1];
ll ifacts[MAXN + 1];
ll infacts[MAXN + 1];

void initialize(){
    facts[0] = 1;
    ifacts[0] = ifacts[1] = 1;
    infacts[0] = infacts[1] = 1;

    for(int i = 1; i <= MAXN; i++)
        facts[i] = (facts[i - 1] * i) % MOD;

    for(int i = 2; i <= MAXN; i++)
        infacts[i] = infacts[MOD % i] * (MOD - MOD / i) % MOD;

    for(int i = 2; i <= MAXN; i++)
        ifacts[i] = (infacts[i] * ifacts[i - 1]) % MOD;
}

int ncr(int n, int r){
    return ((facts[n] * ifacts[r]) % MOD * ifacts[n - r]) % MOD;
}

main(){
    initialize();
    
    int t; cin >> t;

    while(t--){
        int n; cin >> n;
        string a, b; cin >> a >> b;

        int x = 0, y = 0, s = 0;

        for(int i = 0; i < n; i++){
            if(a[i] == '1') x++;
            if(b[i] == '1') y++;
        }

        int st = abs(x - y);
        int en = x + y;

        if(en > n)
            en = 2 * n - x - y;

        for(int r = st; r <= en; r += 2)
            s = (s + ncr(n, r)) % MOD;

        cout << s << endl;
    }
}
