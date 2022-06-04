#include <bits/stdc++.h>

using namespace std;

int main() {
    // your code goes here
    int T;
    cin >> T;
    while (T--) {
        int n; cin >> n;
        string s; cin >> s;

        int ans = 0;
        for (int i = 0; i < n; i++) {
            if ((i+1 < n) && (s[i] == s[i+1])) {
                ans = ans + 1;
                i++;

            } else {
                ans = ans + 1;
            }
        }
        cout << ans << endl;
    }
    return 0;
}
