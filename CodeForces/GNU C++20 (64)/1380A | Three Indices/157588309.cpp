#include <bits/stdc++.h>
 
using namespace std;
 
#define ll long long int
#define mp make_pair
#define pb push_back
#define tc int t; cin >> t; while(t--)
#define imax INT_MAX
#define imin INT_MIN
#define llmax LLONG_MAX
#define llmin LLONG_MIN
#define nl "\n"
#define pminheap priority_queue<pair<int, int> , vector<pair<int , int>> , greater<pair<int , int>>>
#define minheap priority_queue<int , vector<int> , greater<int>>
#define maxheap priority_queue<int>
#define zeroMatrix vector<vector<int>> v(n , vector<int>(n , 0))
 
 
int main() {
    tc {
        ll n;
        cin >> n;
 
        vector<ll> v;
        pminheap right;
        for (ll i = 0; i < n; i++) {
            ll x;
            cin >> x;
            v.pb(x);
            if (i > 1)right.push({x, i});
        }
 
        ll a, b, c;
        pminheap left;
        left.push({v[0], 0});
        bool flag = 0;
 
        if (n > 2) {
            ll i;
            for (i = 1; i < n - 1; i++) {
                if (right.top().second == i) {
                    right.pop();
 
                } else {
                    if (v[i] > left.top().first && v[i] > right.top().first) {
                        if (left.top().second < i && i < right.top().second) {
                            a = left.top().second + 1;
                            b = i + 1;
                            c = right.top().second + 1;
                            flag = 1;
                            break;
                        }
                    }
                }
 
                left.push({v[i], i});
            }
        }
 
        if (!flag) cout << "NO" << nl;
        else cout << "YES" << nl << a << " " << b << " " << c << nl;
    }
    return 0;
}