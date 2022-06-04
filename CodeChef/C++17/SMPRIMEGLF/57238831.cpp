#include <bits/stdc++.h>
using namespace std;

bool is_prime(int n) {
    for (int i = 2; i * i <= n; i++)
        if (n % i == 0)
            return false;

    return true;
}

signed main() {
    int n; cin >> n;
    n++;

    while (!is_prime(n))
        n++;
    
    cout << n << endl;
}
