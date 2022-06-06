#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
 
using pi = pair<int, int>;
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
int n, m, i, j;
 
pi farthest(int a, int b) {
    pair<int, pi> v1 = { abs(a-1) + abs(b-1), {1, 1} };
    pair<int, pi> v2 = { abs(a-1) + abs(b-m), {1, m} };
    pair<int, pi> v3 = { abs(a-n) + abs(b-1), {n, 1} };
    pair<int, pi> v4 = { abs(a-n) + abs(b-m), {n, m} };
 
    return max({v1, v2, v3, v4}).second;
}
 
signed main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
 
    int t;
    cin >> t;
    while (t--) {
        cin >> n >> m >> i >> j;
 
        pair<int, int> fc = farthest(i, j);
        pair<int, int> sc = {
                (fc.first == 1) ? n : 1,
                (fc.second == 1) ? m : 1
        };
 
        cout << fc.first << " " << fc.second << " " << sc.first << " " << sc.second << endl;
    }
}