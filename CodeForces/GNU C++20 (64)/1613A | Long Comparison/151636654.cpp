#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int tc; cin >> tc;
    while (tc--) {
        string x; int p;
        cin >> x >> p;
 
        string y; int q;
        cin >> y >> q;
 
        if (x.size() + p == y.size() + q) {
            while (x.size() < y.size()) x.push_back('0'), p--;
            while (y.size() < x.size()) y.push_back('0'), q--;
 
            if (stoi(x) < stoi(y))
                cout << "<" << endl;
            else if (stoi(x) == stoi(y))
                cout << "=" << endl;
            else
                cout << ">" << endl;
 
        } else {
            cout << ((x.size() + p < y.size() + q) ? "<" : ">") << endl;
        }
    }
}