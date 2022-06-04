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
        int n; cin >> n;
        string s; cin >> s;

        int c = 0;

        for(int i = 0; i < n; i++)
            if(s[i] == '1')
                c++;

        cout << c * (c + 1) / 2 << endl;
    }
}
