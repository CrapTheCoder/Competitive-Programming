#include <bits/stdc++.h>

using namespace std;

typedef int integer;
typedef long long int ll;

#define int ll
#define endl '\n'

#define speed ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

integer main(){
    speed;

    int t; cin >> t;

    while(t--){
        int n, k; cin >> n >> k;
        int a[n];

        int ts = 0;

        for(int i = 0; i < n; i++){
            cin >> a[i];
            ts += a[i];
        }

        sort(a, a + n);

        int s = 0;

        for(int i = 0; i < k; i++)
            s += a[i];

        int m1 = max(ts - s, s) - min(ts - s, s);

        s = 0;

        for(int i = n - 1; i > n - 1 - k; i--)
            s += a[i];

        int m2 = max(ts - s, s) - min(ts - s, s);

        cout << max(m1, m2) << endl;
    }
}
