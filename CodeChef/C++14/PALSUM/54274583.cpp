#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        
        vector<int> d;
        int c1 = 0;

        for (int i = 0; (n >> i) > 0; i++) {
            if ((n >> i) & 1) {
                if ((1 << i) - 1 == 0) {
                    c1++; continue;
                }
                
                if ((1 << i) - 1 == 1)
                    c1++;
                else
                    d.push_back((1 << i) - 1);

                c1++;
            }
        }

        if (c1 == 1) {
            d.push_back(1);

        } else if (c1 == 2) {
            d.push_back(1);
            d.push_back(1);

        } else if (c1 == 3) {
            d.push_back(3);

        } else if (c1 == 4) {
            d.push_back(3);
            d.push_back(1);
            
        } else if (c1 == 5) {
            d.push_back(5);
            
        } else if (c1 == 6) {
            d.push_back(5);
            d.push_back(1);
            
        } else if (c1 == 7) {
            d.push_back(7);
            
        } else if (c1 == 8) {
            d.push_back(7);
            d.push_back(1);
            
        } else if (c1 == 9) {
            d.push_back(9);
            
        } else if (c1 == 10) {
            d.push_back(9);
            d.push_back(1);
            
        } else if (c1 == 11) {
            d.push_back(9);
            d.push_back(1);
            d.push_back(1);
        }
        
        cout << d.size() << endl;

        for (auto i : d)
            cout << i << " ";
        cout << endl;
    }
}
