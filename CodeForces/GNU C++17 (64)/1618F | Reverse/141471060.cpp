#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
#define all(iter) (iter).begin(), (iter).end()
#define rall(iter) (iter).rbegin(), (iter).rend()
#define size_of(iter) (int) (iter).size();
 
const int MAX = 1e18 + 13;
 
string itob(int n) {
    if (n == 0)
        return "0";
 
    string s;
    while (n) {
        s += (n & 1) + '0';
        n >>= 1;
    }
 
    reverse(s.begin(), s.end());
    return s;
}
 
int btoi(string s) {
    int n = 0;
    for (int i = 0, j = s.size() - 1; i < s.size(); i++, j--)
        if (s[i] == '1')
            n += 1LL << j;
 
    return n;
}
 
bool check(string s, int y) {
    for (int l = 0; l <= 64; l++) {
        for (int r = 0; r <= 64; r++) {
            if (l + r + s.size() > 64)
                continue;
 
            string ls; for (int i = 0; i < l; i++) ls += '1';
            string rs; for (int i = 0; i < r; i++) rs += '1';
 
            string t = ls + s + rs;
 
            if (btoi(t) == y)
                return true;
        }
    }
 
    return false;
}
 
bool check1(int x, int y) {
    string s = itob(x) + '1';
    return check(s, y);
}
 
bool check2(int x, int y) {
    string s = itob(x);
    reverse(s.begin(), s.end());
 
    s = itob(btoi(s));
    reverse(s.begin(), s.end());
 
    return check(s, y);
}
 
bool check3(int x, int y) {
    string s = itob(x) + '1';
    reverse(s.begin(), s.end());
    return check(s, y);
}
 
bool check4(int x, int y) {
    string s = itob(x);
    reverse(s.begin(), s.end());
 
    s = itob(btoi(s));
    return check(s, y);
}
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int x, y; cin >> x >> y;
 
    if (x == y)
        cout << "YES" << endl;
    else
        cout << ((check1(x, y) || check2(x, y) || check3(x, y) || check4(x, y)) ? "YES" : "NO") << endl;
}