#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    string s, t;
    cin >> s >> t;
 
    int index1 = s.size() - 1;
    int index2 = t.size() - 1;
 
    int longest_suffix = 0;
    while (index1 >= 0 && index2 >= 0 && s[index1] == t[index2]) {
        longest_suffix++;
        index1--;
        index2--;
    }
 
    cout << (s.size() - longest_suffix) + (t.size() - longest_suffix) << endl;
}