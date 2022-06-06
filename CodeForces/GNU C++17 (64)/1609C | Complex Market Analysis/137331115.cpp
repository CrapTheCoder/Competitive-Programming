#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
 
const int MAX = 5e6 + 13;
 
bool sieve[MAX];
set<int> ps;
 
void siever() {
    fill(sieve, sieve + MAX, true);
 
    sieve[0] = sieve[1] = false;
    for (int i = 2; i < MAX; i++) {
        if (sieve[i]) {
            ps.insert(i);
            for (int j = i*i; j < MAX; j += i)
                sieve[j] = false;
        }
    }
}
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
    siever();
 
    int tc; cin >> tc;
 
    while (tc--) {
        int m, e; cin >> m >> e;
        int b[m];
        for (int i = 0; i < m; i++)
            cin >> b[i];
        
        int c = 0;
        for (int i = 0; i < e; i++) {
            vector<int> a;
            for (int j = i; j < m; j += e)
                a.push_back(b[j]);
            
            int n = a.size();
 
            int f = 1;
            int prime = -1;
            deque<int> ones;
 
            for (int right = 0; right < n; right++) {
                f *= a[right];
                if (a[right] == 1)
                    ones.push_back(right);
                
                if (ps.count(f)) {
                    if (ps.count(a[right]))
                        prime = right;
                    
                } else if (f != 1) {
                    if (ps.count(a[right])) {
                        while (!ones.empty() && ones[0] < prime)
                            ones.pop_front();
                        
                        prime = right;
                        f = a[right];
 
                    } else {
                        prime = -1;
                        ones.clear();
                        f = 1;
                    }
                }
 
                int left = -1;
                if (!ones.empty())
                    left = ones[0];
 
                if (prime != -1) {
                    if (left != -1 && left < prime)
                        c += prime - left;
                    
                    if (right - prime > 0)
                        c++;
                }
            }
        }
 
        cout << c << endl;
    }
}