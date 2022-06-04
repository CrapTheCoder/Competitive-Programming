#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int tcs; cin >> tcs;

    while (tcs--) {
        int n; cin >> n;
        string s; cin >> s;

        stack<char> d;
        int current = 0;
        int answer = 0;

        for (int i = 0; i < n; i++) {
            if (d.empty() || (d.top() != s[i])) {
                current = 0;
                d.push(s[i]);

            } else {
                current++;
                d.pop();
                answer = max(answer, current);
            }
        }

        cout << answer << endl;
    }
}
