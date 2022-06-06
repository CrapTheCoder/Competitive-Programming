#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    string s; cin >> s;
 
    int c = 0;
    for (auto i : s)
        if (i == '4' || i == '7')
            c++;
 
    string res = to_string(c);
 
    bool flag = false;
    for (auto i : res)
        if (i != '4' && i != '7')
            flag = true;
 
    if (flag)
        cout << "NO" << endl;
    else
        cout << "YES" << endl;
}