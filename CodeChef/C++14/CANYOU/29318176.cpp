#include <bits/stdc++.h>
using namespace std;

typedef int integer;
typedef long long int ll;

#define int ll
#define endl '\n'

const int MAX = 32;

integer main()
{
    ios::sync_with_stdio(false); cin.tie(NULL);

    int n; cin >> n;

    int p[n+1][MAX] = {0};

    for(int i = 1; i <= n; i++){
        int x; cin >> x;

        int ind = MAX - 1;

        while(x > 0){
            p[i][ind--] = x & 1;
            x >>= 1;
        }
    }

    for(int i = 1; i <= n; i++)
        for(int j = 0; j < MAX; j++)
            p[i][j] += p[i-1][j];

    int q; cin >> q;

    while(q--){
        int l, r, k; cin >> l >> r >> k;

        bool found = false;

        for(int i = 0; i < MAX; i++){
            if(p[r][i] - p[l-1][i] >= k){
                found = true;
                break;
            }
        }

        if(found)
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
}
