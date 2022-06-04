#include <bits/stdc++.h>

using namespace std;

bool compare(const pair<int, int> &s, const pair<int, int> &d){
    if(s.first < d.first) return true;
    if(s.first > d.first) return false;

    return s.second < d.second;
}

int main()
{
    ios::sync_with_stdio(false); cin.tie(NULL);

    int n; cin >> n;

    pair<int, int> a[n];

    for(int i = 0; i < n; i++){
        cin >> a[i].first >> a[i].second;
        a[i].second += a[i].first;
    }

    sort(a, a + n, compare);

    int dp[n];

    for(int i = 0; i < n; i++){
        dp[i] = 1;

        for(int j = i - 1; j >= 0; j--){
            if(a[j].second < a[i].first){
                dp[i] = dp[j] + 1;
                break;
            }
        }
    }

    cout << *max_element(dp, dp + n) << endl;
}
