#include <bits/stdc++.h>

using namespace std;

typedef int integer;
typedef long long int ll;

#define int ll

#define endl '\n'

integer main(){
    ios::sync_with_stdio(false); cin.tie(NULL);

    int q; cin >> q;

    set<int> s;

    while(q--){
        int t, n; cin >> t >> n;

        if(t == 1)
            s.insert(n);

        if(t == 2)
            cout << (s.count(n) ? "Yes" : "No") << endl;

        if(t == 3){
            auto i = s.upper_bound(n);

            if(i != s.end())
                cout << *(s.upper_bound(n)) << endl;
            else
                cout << -1 << endl;
        }
    }
}
