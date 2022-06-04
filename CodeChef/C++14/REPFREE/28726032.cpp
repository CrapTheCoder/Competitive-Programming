#include <bits/stdc++.h>
using namespace std;

typedef long long int ll;

const ll MAX = 987654321LL;

bool check(ll n){
    bool a[10]; fill(a, a + 10, false);

    while(n > 0){
        int x = n % 10;

        if(x == 0 || a[x] == true)
            return false;

        a[x] = true;

        n /= 10;
    }

    return true;
}

int main()
{
    ll n; cin >> n;

    for(ll i = n + 1; i <= MAX; i++){
        if(check(i)){
            cout << i << endl;
            return 0;
        }
    }

    cout << 0 << endl;
}
