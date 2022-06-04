#include <bits/stdc++.h>
using namespace std;

int main(){
    int n; cin >> n;
    int a[n];
    int dp[n];

    int s = 0;

    for(int i = 0; i < n; i++){
        cin >> a[i];

        dp[i] = 1;

        for(int j = 0; j < i; j++)
            a[j] < a[i]? dp[i] += dp[j] : 0;

        s += dp[i];
    }

    cout << s << endl;
}
