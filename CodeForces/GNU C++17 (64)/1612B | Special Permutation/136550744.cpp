#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
bool check(vector<int> left, vector<int> right, int a, int b, int n) {
    if (left.size() != right.size() || left.size() + right.size() != n)
        return false;
 
    if (*min_element(left.begin(), left.end()) != a || *max_element(right.begin(), right.end()) != b)
        return false;
    
    return true;
}
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int tc; cin >> tc;
 
    while (tc--) {
        int n, a, b;
        cin >> n >> a >> b;
 
        set<int> valid;
        for (int i = 1; i <= n; i++)
            valid.insert(i);
        
        vector<int> left, right;
        left.push_back(a); valid.erase(a);
        right.push_back(b); valid.erase(b);
 
        int ta = a, tb = b;
        if (a < b) swap(ta, tb);
 
        for (int i = ta+1; i <= n; i++) {
            left.push_back(i); valid.erase(i);
        }
    
        for (int i = 1; i < tb; i++) {
            right.push_back(i); valid.erase(i);
        }
 
        for (auto i : valid) {
            if (left.size() < n / 2)
                left.push_back(i);
            else
                right.push_back(i);
        }
        
        if (!check(left, right, a, b, n)) {
            cout << -1 << endl; continue;
        }
 
        for (auto i : left) cout << i << " ";
        for (auto i : right) cout << i << " ";
        cout << endl;
    }
}