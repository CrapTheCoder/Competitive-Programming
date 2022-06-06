#include <bits/stdc++.h>
using namespace std;
 
signed main() {
    int a, b; cin >> a >> b;
 
    for (int cur = 1; ; cur++) {
        (cur % 2) ? (a -= cur) : (b -= cur);
        if (a < 0) { cout << "Vladik" << endl; break; }
        if (b < 0) { cout << "Valera" << endl; break; }
    }
}