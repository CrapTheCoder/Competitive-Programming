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
 
        if (a < b) {
            vector<int> left, right;
 
            for (int i = b+1; i <= n; i++) {
                left.push_back(i); valid.erase(i);
            }
            
            left.push_back(a); valid.erase(a);
 
            for (int i = 1; i < a; i++) {
                right.push_back(i); valid.erase(i);
            }
            
            right.push_back(b); valid.erase(b);
 
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
 
        } else {
            vector<int> left, right;
 
            for (int i = a+1; i <= n; i++) {
                left.push_back(i); valid.erase(i);
            }
            
            left.push_back(a); valid.erase(a);
 
            for (int i = 1; i < b; i++) {
                right.push_back(i); valid.erase(i);
            }
            
            right.push_back(b); valid.erase(b);
 
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
}