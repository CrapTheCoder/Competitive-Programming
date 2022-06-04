#include<bits/stdc++.h>
using namespace std;
#define int long long int

int arr[10000013] = {};

void sieve(int n){
    for (int i = 2; i <= n; i++){
        if (arr[i] == 1){
            for (int j = i * i; j <= n; j += i){
                arr[j] = 0;
            }
        }

        arr[i] += arr[i-1];
    }
}

void solve(void)
{
    int a,b;cin>>a>>b;
    cout << arr[b] - arr[a-1] << endl;

    return;
}

int32_t main()
{
    fill(arr, arr + 10000010, 1);
    sieve(1e7 + 10);

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin>>t;
    while (t--)
    {
        solve();
    }

    return 0;
}