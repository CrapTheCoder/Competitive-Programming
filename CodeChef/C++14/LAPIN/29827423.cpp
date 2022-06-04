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
        string s; cin >> s;
        int n = s.size();

        string l, r;

        for(int i = 0; i < n / 2; i++)
            l += s[i];

        for(int i = n / 2 + n % 2; i < n; i++)
            r += s[i];

        sort(l.begin(), l.end());
        sort(r.begin(), r.end());

        if(l == r)
            cout << "YES";
        else
            cout << "NO";

        cout << endl;
    }
}
