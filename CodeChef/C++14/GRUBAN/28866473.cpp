#include <bits/stdc++.h>
using namespace std;

typedef int integer;
typedef long long int ll;

#define int ll

integer main()
{
    int t; cin >> t;

    while(t--){
        int n, k; cin >> n >> k;
        int x = k * (k + 1) / 2;

        int maxi = -1;

        for(int i = 1; (i * x <= n) && (i <= sqrt(n)); i++){
            if(n % i != 0)
                continue;

            maxi = max(maxi, i);

            if(n / i * x <= n)
                maxi = max(maxi, n / i);
        }

        cout << maxi << endl;
    }
}
