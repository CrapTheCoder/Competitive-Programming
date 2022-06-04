#include <bits/stdc++.h>

using namespace std;

int main() {
    int t; cin >> t;

    string s;
    while (cin >> s) {
        reverse(s.begin(), s.end());

        for (int i = 0; i < s.size(); i++)
            s[i] = tolower(s[i]);

        cout << s << endl;
    }
}
