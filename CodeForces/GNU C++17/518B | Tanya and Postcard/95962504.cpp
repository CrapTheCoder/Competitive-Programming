#include <bits/stdc++.h>
using namespace std;
 
#define endl '\n'
 
signed main() {
 string s; cin >> s;
 string t; cin >> t;
 bool r[s.size()] = {false};
 
 map<char, int> counter;
 
 int c1 = 0, c2 = 0;
 
 for (auto i : t)
        counter[i]++;
 
    for (int i = 0; i < s.size(); i++) {
        if (counter[s[i]]) {
            c1++;
            counter[s[i]]--;
 
        } else {
            r[i] = true;
        }
    }
 
    for (int i = 0; i < s.size(); i++) {
        if (!r[i])
            continue;
 
        if ('a' <= s[i] && s[i] <= 'z') {
            s[i] -= 'a';
            s[i] += 'A';
 
        } else {
            s[i] -= 'A';
            s[i] += 'a';
        }
 
        if (counter[s[i]]) {
            c2++;
            counter[s[i]]--;
        }
    }
 
    cout << c1 << " " << c2 << endl;
}