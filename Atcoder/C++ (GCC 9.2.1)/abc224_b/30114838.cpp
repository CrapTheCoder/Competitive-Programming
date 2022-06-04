//Author: Shivank
#include<bits/stdc++.h>

using namespace std; using ll = long long int;
#define tc int t; cin >> t; while(t--)

char add(char c, int i) {
    return (c - 'a' + i) % 26 + 'a';
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(nullptr);

    string s, t;
    cin >> s >> t;

    for (int k = 0; k < 26; k++) {
        bool flag = false;
        for (int i = 0; i < s.size(); i++) {
            if (add(s[i], k) != t[i]) {
                flag = true;
            }
        }

        if (!flag) {
            cout << "Yes" << endl;
            return 0;
        }
    }

    cout << "No" << endl;
}
