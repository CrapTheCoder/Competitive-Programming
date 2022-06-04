#include <bits/stdc++.h>
using namespace std;
 
#define int long long
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
map<int, bool> queries;
 
bool query(int value) {
    if (value > 100)
        return false;
    
    if (queries.contains(value))
        return queries[value];
 
    cout << value << endl;
    string inp; cin >> inp;
    return queries[value] = (inp == "yes");
}
 
vector<int> ps = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47};
 
signed main() {
    vector<int> a;
    for (auto p: ps)
        if (query(p))
            a.push_back(p);
 
    if (a.size() == 0 || (a.size() == 1 && !query(a[0] * a[0])))
        cout << "prime" << endl;
    else
        cout << "composite" << endl;
}