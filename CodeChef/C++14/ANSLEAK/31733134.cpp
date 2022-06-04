#include<bits/stdc++.h>
#include<random>
#include<ctime>
using namespace std;

#define int long long
#define endl '\n'

signed main()
{
    srand(time(NULL));

    ios::sync_with_stdio(false); cin.tie(NULL);

    int t; cin >> t;

    while(t--){
        int n, m, k; cin >> n >> m >> k;

        for(int _ = 0; _ < n; _++){
            int a[k];

            for(int i = 0; i < k; i++)
                cin >> a[i];

            cout << a[rand() % k] << " ";
        }

        cout << endl;
    }
}
