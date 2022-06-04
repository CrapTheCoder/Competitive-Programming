#include <bits/stdc++.h>
using namespace std;

#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;

#define ordered_set tree<pair<int, int>, null_type, less_equal<pair<int, int>>, rb_tree_tag, tree_order_statistics_node_update>

#define int long long
#define endl '\n'

int power(int x, unsigned int y, int p) {
    int res = 1;
    x = x % p;

    while (y > 0) {
        if (y & 1)
            res = (res*x) % p;

        y = y>>1;
        x = (x*x) % p;
    }
    return res;
}

bool miller(int d, int n) {
    int a = 2 + rand() % (n - 4);
    int x = power(a, d, n);

    if (x == 1 || x == n-1)
       return true;

    while (d != n-1)
    {
        x = (x * x) % n;
        d *= 2;

        if (x == 1) return false;
        if (x == n-1) return true;
    }

    return false;
}

bool isp(int n, int k) {
    if (n <= 1 || n == 4) return false;
    if (n <= 3) return true;

    int d = n - 1;
    while (d % 2 == 0)
        d /= 2;

    for (int i = 0; i < k; i++)
         if (!miller(d, n))
              return false;

    return true;
}

main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int t; cin >> t;

    while (t--) {
        int n, x;
        cin >> n >> x;

        int a[n];
        for (int i = 0; i < n; i++)
            cin >> a[i];

        int sum = 0;
        ordered_set s;

        for (int i = 0; i < x; i++) {
            s.insert({a[i], i});
            sum += a[i];
        }

        int c = 0;

        int avg = sum / x;
        int med = (*s.find_by_order(x/2 - (1-x%2))).first;
        if ((avg >= med) && (isp(avg, 50) == isp(med, 50)))
            c++;

        for (int i = x; i < n; i++) {
            s.erase(s.upper_bound({a[i-x], i-x}));
            s.insert({a[i], i});

            sum += a[i] - a[i-x];

            int avg = sum / x;
            int med = (*s.find_by_order(x/2 - (1-x%2))).first;
            if ((avg >= med) && (isp(avg, 50) == isp(med, 50)))
                c++;
        }

        cout << c << endl;
    }
}
