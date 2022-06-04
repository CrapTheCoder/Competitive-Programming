#include <bits/stdc++.h>
using namespace std;

typedef int integer;
typedef long long int ll;

#define int ll
#define endl '\n'

#define MOD 1000000007

void multiply(vector<int> a[], vector<int> b[], vector<int> x[], int r1, int c1, int c2){
    vector<int> c[r1];

    for(int i = 0; i < r1; i++)
        c[i].resize(c2);

    for(int i = 0; i < r1; i++)
        for(int j = 0; j < c2; j++)
            for(int k = 0; k < c1; k++)
                c[i][j] = (c[i][j] + (a[i][k] * b[k][j]) % MOD) % MOD;

    for(int i = 0; i < r1; i++)
        for(int j = 0; j < c2; j++)
            x[i][j] = c[i][j];
}

void power(vector<int> x[], int n){
    vector<int> res[4] = {
                            {1, 0, 0, 0},
                            {0, 1, 0, 0},
                            {0, 0, 1, 0},
                            {0, 0, 0, 1}
                         };

    while(n > 0){
        if(n % 2)
            multiply(res, x, res, 4, 4, 4);

        n /= 2;
        multiply(x, x, x, 4, 4, 4);
    }

    for(int i = 0; i < 4; i++)
        for(int j = 0; j < 4; j++)
            x[i][j] = res[i][j];
}

integer main()
{
    ios::sync_with_stdio(false); cin.tie(NULL);

    int t; cin >> t;

    while(t--){
        int n; cin >> n;

        vector<int> magic[4] = {
                                {36, 0, 0, 0},
                                {1, 36, 0, 0},
                                {0, 36, 36, 0},
                                {36, 0, 0, 1}
                               };

        power(magic, n);

        vector<int> orig[4] = {{1, 36, 36, 1}};

        multiply(orig, magic, orig, 1, 4, 4);

        cout << orig[0][0] << endl;
    }
}
