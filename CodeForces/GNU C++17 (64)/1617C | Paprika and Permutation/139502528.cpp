#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
#define all(iter) (iter).begin(), (iter).end()
#define rall(iter) (iter).rbegin(), (iter).rend()
#define size_of(iter) (int) iter.size();
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int tc; cin >> tc;
    while (tc--) {
        int n; cin >> n;
        
        set<int> miss;
        vector<int> rest;
        
        int a[n+1];
        for (int i = 1; i <= n; i++) {
            cin >> a[i];
            miss.insert(i);
        }
        
        for (int i = 1; i <= n; i++) {
            if (miss.count(a[i]))
                miss.erase(a[i]);
            else
                rest.push_back(a[i]);
        }
 
        sort(all(rest));
 
        int c = 0; bool flag = false;
        int ind = 0;
 
        for (int i : miss) {
            if (rest[ind] - i <= 0) {
                flag = true;
                break;
            }
 
            if (rest[ind] % (rest[ind] - i) == i) {
                c++;
 
            } else {
                flag = true;
                break;
            }
 
            ind++;
        }
 
        if (flag)
            cout << -1;
        else
            cout << c;
        
        cout << endl;
    }
}