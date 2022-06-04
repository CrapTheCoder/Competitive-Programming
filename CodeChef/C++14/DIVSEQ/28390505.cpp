#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;

int main() {
    iostream::sync_with_stdio(false); cin.tie(NULL);

    int n; cin >> n;

    int a[n];
    int dp[n];

    for(int i = 0; i < n; i++)
        cin >> a[i];

    int maxi = 1;

    for(int i = 0; i < n; i++){
        dp[i] = 1;

        for(int j = i - 1; j >= 0; j--){
            if(a[i] % a[j] == 0 && dp[i] <= dp[j])
                dp[i] = dp[j] + 1;
        }

        if(maxi < dp[i])
            maxi = dp[i];
    }

    cout << maxi;

    return 0;
}
