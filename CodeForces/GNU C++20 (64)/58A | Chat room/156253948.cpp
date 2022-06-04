#include <bits/stdc++.h>
using namespace std;
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    string s; cin >> s;
    string t = "hello";
 
    int j = 0;
    for (int i = 0; i < s.size() && j < t.size(); i++)
        if (s[i] == t[j])
            j++;
 
    cout << (j == t.size() ? "YES" : "NO") << endl;
}