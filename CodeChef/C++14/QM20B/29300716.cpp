#include <bits/stdc++.h>
using namespace std;

typedef int integer;
typedef long long int ll;

#define int ll

#define endl '\n'

integer main(){
    ios::sync_with_stdio(false); cin.tie(NULL);

    int n, m; cin >> n >> m;

    int a[n][m];

    for(int i = 0; i < n; i++){
        string s; cin >> s;

        for(int j = 0; j < m; j++){
            a[i][j] = 0;

            if(i != 0){
                for(int k = max(0LL, j - 1); k < min(m, j + 2); k++){
                    a[i][j] = max(a[i][j], a[i-1][k]);
                }
            }

            a[i][j] += s[j] - '0';
        }
    }

    cout << *max_element(a[n - 1], a[n - 1] + m) << endl;
}
