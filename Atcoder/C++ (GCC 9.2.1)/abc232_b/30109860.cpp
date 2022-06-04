//Author: Shivank
#include<bits/stdc++.h>

using namespace std; using ll = long long int;
#define tc int t; cin >> t; while(t--)

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(nullptr);

    string s, t;
    cin >> s >> t;

    set<int> diff;
    for (int i = 0; i < s.size(); i++)
        diff.insert(((s[i] - t[i]) + 26) % 26);

    if (diff.size() == 1)
        cout << "Yes" << endl;
    else
        cout << "No" << endl;
}
