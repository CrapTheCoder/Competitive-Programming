#include <bits/stdc++.h>

using namespace std;

int main(){
    int n; cin >> n;

    int a[n];

    for(int i = 0; i < n; i++)
        cin >> a[i];

    int max_now = -1;

    for(int i = 0; i < n; i++)
        max_now = max(max_now, 1 + i + a[i]);

    int ans[n] = {0}; ans[0] = max_now;

    for(int i = 0; i < n - 1; i++){
        max_now = max(max_now - 1, a[i] + n);
        ans[n - i - 1] = max_now;
    }

    for(int i = 0; i < n; i++)
        cout << ans[i] << " ";
}
