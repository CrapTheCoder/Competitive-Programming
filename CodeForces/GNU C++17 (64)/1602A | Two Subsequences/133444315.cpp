#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
using namespace std;
 
const int INF = LLONG_MAX >> 1;
 
signed main(){
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int tc; cin >> tc;
 
    while (tc--) {
        string s; cin >> s;
 
        char a = s[0];
        for (auto i : s)
            a = min(a, i);
 
        string b;
        bool flag = false;
        for (auto i : s) {
            if (flag || i != a)
                b += i;
            else
                flag = true;
        }
 
        cout << a << " " << b << endl;
    }
}