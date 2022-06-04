#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    int t; cin >> t;

    while(t--){
        int n; cin >> n;
        int p[n+1]; p[0] = 0;

        for(int i = 1; i <= n; i++){
            int v; cin >> v;

            p[i] = p[i - 1];

            if(!(v & 1))
                p[i]++;
        }

        int q; cin >> q;

        while(q--){
            int l, r; cin >> l >> r;

            if(!(p[r] - p[l - 1]))
                cout << "ODD";
            else
                cout << "EVEN";

            cout << endl;
        }
    }
}
