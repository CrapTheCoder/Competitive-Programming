#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t; cin >> t;

    while (t--) {
        string s; cin >> s;

        sort(s.begin(), s.end());

        int c = 0;

        int n = stoi(s);
        if (n % 7 == 0)
            c++;

        while (next_permutation(s.begin(), s.end())) {
            n = stoi(s);
            if (n % 7 == 0)
                c++;
        }

        cout << c << endl;
    }
}
