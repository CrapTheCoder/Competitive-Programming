#include <bits/stdc++.h>
using namespace std;

int main()
{
    long long int n, m; cin >> n >> m;
    long long int x = ceil(m / 2 * n + (m % 2 * 0.5) * n);

    cout << x << endl;

    return 0;
}
