#include <bits/stdc++.h>

using namespace std;

typedef int integer;
typedef long long int ll;

#define int ll
#define endl '\n'

integer main(){
    ios::sync_with_stdio(false); cin.tie(NULL);

    int n; cin >> n;

    int a[n]; for(int i = 0; i < n; i++) cin >> a[i];
    int b[n]; for(int i = 0; i < n; i++) cin >> b[i];

    int add = 0;

    int c = 0;

    for(int i = n - 1; i >= 0; i--){
        int x;

        if((a[i] + add) % b[i] == 0)
            x = 0;
        else
            x = b[i] - (a[i] + add) % b[i];

        add += x;
        c += (i + 1) * x;
    }

    cout << c;
}
