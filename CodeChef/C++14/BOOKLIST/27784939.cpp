#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n; cin >> n;
    vector<int> v;

    for(int i = 0; i < n; i++){
        int x; cin >> x;
        v.push_back(x);
    }

    int m; cin >> m;

    for(int _ = 0; _ < m; _++){
        int i; cin >> i; i--;
        cout << v[i] << endl;

        v.erase(v.begin() + i, v.begin() + i + 1);
    }

    return 0;
}

