#include <bits/stdc++.h>
using namespace std;

typedef int integer;
typedef long long int ll;

#define int ll
#define endl '\n'

#define mod 1000000007

#define speed ios::sync_with_stdio(false); cin.tie(NULL);

void mul(vector<int> x[2], vector<int> y[2]){
	int a = (x[0][0] % mod * y[0][0] % mod) % mod + (x[0][1] % mod * y[1][0] % mod) % mod;
	int b = (x[0][0] % mod * y[0][1] % mod) % mod + (x[0][1] % mod * y[1][1] % mod) % mod;
	int c = (x[1][0] % mod * y[0][0] % mod) % mod + (x[1][1] % mod * y[1][0] % mod) % mod;
	int d = (x[1][0] % mod * y[0][1] % mod) % mod + (x[1][1] % mod * y[1][1] % mod) % mod;

	x[0][0] = a % mod; x[0][1] = b % mod;
	x[1][0] = c % mod; x[1][1] = d % mod;
}

integer main(){
    speed;

    int t; cin >> t;

    while(t--){
        int n, m; cin >> n >> m;

        int x = m % mod;
        int ans = (x * x) % mod;

        m = (m - 1) % mod;

        vector<int> a[2] = {{m, 1}, {m, 0}};
        vector<int> b[2] = {{1, 0}, {0, 1}};

        --n;

        while(n != 0){
            if(n % 2)
                mul(b, a);

            mul(a, a);
            n /= 2;
        }

        ans = ((b[0][1] * ans) % mod + (b[1][1] * x) % mod) % mod;

        cout << ans << endl;
    }
}
