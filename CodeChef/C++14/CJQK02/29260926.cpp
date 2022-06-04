#include<bits/stdc++.h>
using namespace std;

typedef int integer;
typedef long long int ll;

#define int ll

integer main(){
    int t = 1;
    // cin >> t;

    while(t--){
        int n, x, y; cin >> n >> x >> y;

        if(n == 1){
            if(x != y)
                cout << 0 << endl;
            else
                cout << 1 << endl;

            continue;
        }

        if(y < x){
            cout << 0 << endl;
            continue;
        }

        cout << (y * (n - 1) + x) - (x * (n - 1) + y) + 1 << endl;
    }
}
