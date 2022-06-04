#include <bits/stdc++.h>

using namespace std;

typedef int integer;
typedef long long int ll;

#define int ll
#define endl '\n'

#define speed ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

integer main(){
    speed;

    int n, q; cin >> n >> q;

    set<int> s;

    for(int i = 0; i < n; i++){
        int v; cin >> v;
        s.insert(v);
    }

    for(int i = 0; i < q; i++){
        int v; cin >> v;

        auto it = s.upper_bound(v);

        if(it != s.begin())
            cout << *(--it) << endl;
        else
            cout << -1 << endl;
    }

    return 0;
}
