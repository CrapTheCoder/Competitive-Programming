#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t; cin >> t;
    
    while (t--) {
        string s; cin >> s;
        string p; cin >> p;
        
        unordered_map<char, int> sc;
        
        for (char i: s) ++sc[i];
        for (char i: p) --sc[i];
        
        string d;
        
        for (pair<char, int> ci: sc)
            for (int i = 0; i < ci.second; i++)
                d += ci.first;
        
        sort(d.begin(), d.end());
        
        char first = '~';
        bool flag = false;
        
        string mini = d + p;
        
        for (int i = 0; i < d.size(); i++) {
            if (d[i] >= p[0]) {
                if (first == '~') {
                    first = d[i];
                    mini = min(mini, string(&d[0], &d[i]) + p + string(&d[i], &d[d.size()]));
                } else if (d[i] != first && flag == false) {
                    flag = true;
                    mini = min(mini, string(&d[0], &d[i]) + p + string(&d[i], &d[d.size()]));
                }
            }
        }
        
        cout << mini << endl;
    }
}
