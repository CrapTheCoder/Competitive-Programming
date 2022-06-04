#include <bits/stdc++.h>

using namespace std;

typedef int integer;
typedef long long int ll;

#define int ll
#define endl '\n'

#define INF numeric_limits<float>::infinity()
#define MOD 1000000007

integer main(){
    int tests; cin >> tests;

    while(tests--){
        int a[3];
        cin >> a[0] >> a[1] >> a[2];

        sort(a, a + 3);

        a[2] -= a[1];
        a[1] = 0;

        a[2] -= a[0];
        a[0] = 0;

        if(a[2] >= 2)
            cout << "No" << endl;
        else
            cout << "Yes" << endl;
    }
}
