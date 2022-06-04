#include <bits/stdc++.h>
using namespace std;

typedef long long int ll;

int n, k;
int a[1000000];

int solve(){
    int dp1[n]; fill(dp1, dp1 + n, INT_MIN);
    int dp2[n]; fill(dp1, dp1 + n, INT_MIN);

    dp1[k] = 0;

    for(int i = k + 1; i < n; i++){
        dp1[i] = dp1[i - 1];

        if(i - 2 >= 0)
            dp1[i] = max(dp1[i], dp1[i - 2]);

        dp1[i] += a[i];
    }

    dp2[0] = a[0];

    for(int i = 1; i < n; i++){
        dp2[i] = dp2[i - 1];

        if(i - 2 >= 0)
            dp2[i] = max(dp2[i], dp2[i - 2]);

        dp2[i] += a[i];
    }

    int maxi = INT_MIN;

    for(int i = k; i < n; i++)
        maxi = max(maxi, dp1[i] + dp2[i] - a[i]);

    return maxi;
}

int main(){
    cin >> n >> k;

    for(int i = 0; i < n; i++)
        cin >> a[i];

    k--;

    cout << solve() << '\n';
}
